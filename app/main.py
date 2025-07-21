from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import speech_recognition as sr
from PIL import Image
import google.generativeai as genai
import os
from dotenv import load_dotenv
import spacy
from transformers import pipeline
import torch
import requests
from io import BytesIO
from typing import List, Dict, Any
import logging

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust to match your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("gemini_api_key")
hugging_token = os.getenv("hugging_face_token")

# Configure Gemini AI
genai.configure(api_key=gemini_api_key)

# Initialize NLP and sentiment analysis models
nlp = spacy.load("en_core_web_sm")
sentimental_analyzer = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# In-memory storage for memories
memories = []

# Pydantic model for text input
class TextInput(BaseModel):
    text: str

# Pydantic model for structured memory output
class StructuredMemory(BaseModel):
    original: str
    events: List[str]
    entities: List[str]
    keywords: List[str]
    sentiment: str
    sentiment_score: float

# Endpoint to handle text input
@app.post("/api/text-input")
async def add_text_input(text_input: TextInput):
    try:
        if text_input.text.strip():
            memories.append(text_input.text.strip())
            return {"message": "Text added to memories", "memory": text_input.text}
        else:
            raise HTTPException(status_code=400, detail="Text input is empty")
    except Exception as e:
        logging.error(f"Error in text input: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Endpoint for speech-to-text
@app.post("/api/speech-to-text")
async def speech_to_text(file: UploadFile = File(...)):
    try:
        # Save uploaded audio file temporarily
        audio_path = f"temp_{file.filename}"
        with open(audio_path, "wb") as f:
            f.write(await file.read())

        r = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
        
        # Clean up temporary file
        os.remove(audio_path)

        if text.strip():
            memories.append(text.strip())
            return {"message": "Speech converted to text", "text": text}
        else:
            raise HTTPException(status_code=400, detail="No text recognized from audio")
    except Exception as e:
        logging.error(f"Error in speech-to-text: {str(e)}")
        if os.path.exists(audio_path):
            os.remove(audio_path)
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Endpoint for image analysis
@app.post("/api/image-analysis")
async def image_analysis_endpoint(file: UploadFile = File(...)):
    try:
        # Open image from uploaded file
        image = Image.open(BytesIO(await file.read()))
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = (
            "Analyze the image and generate a detailed, vivid description that captures the visual elements, mood, atmosphere, "
            "and possible stories or emotions present. The description should be rich enough for someone to imagine the scene clearly, "
            "including context, cultural or social significance, and details that might enrich a memory mosaic."
        )
        response = model.generate_content([prompt, image])

        if response.text.strip():
            memories.append(response.text.strip())
            return {"message": "Image analyzed", "description": response.text}
        else:
            raise HTTPException(status_code=400, detail="No description generated from image")
    except Exception as e:
        logging.error(f"Error in image analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Endpoint for NLP extraction
@app.get("/api/nlp-extraction")
async def nlp_extraction():
    try:
        structured = []
        for mem in memories:
            doc = nlp(mem)
            events = [sent.text for sent in doc.sents]
            entities = [ent.text for ent in doc.ents]
            keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
            structured.append({
                "original": mem,
                "events": events,
                "entities": entities,
                "keywords": keywords
            })
        return {"message": "NLP extraction completed", "structured_memories": structured}
    except Exception as e:
        logging.error(f"Error in NLP extraction: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Endpoint for sentiment analysis
@app.post("/api/sentiment-analysis")
async def sentiment_analysis(structured_memories: List[Dict[str, Any]]):
    try:
        for item in structured_memories:
            result = sentimental_analyzer(
                item["original"],
                candidate_labels=["positive", "neutral", "negative"]
            )
            item["sentiment"] = result["labels"][0]
            item["sentiment_score"] = result["scores"][0]
        return {"message": "Sentiment analysis completed", "sentimental_memories": structured_memories}
    except Exception as e:
        logging.error(f"Error in sentiment analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Endpoint to prepare LLM prompt
@app.post("/api/prepare-llm-prompt")
async def prepare_llm_prompt(sentimental_memories: List[StructuredMemory]):
    try:
        prompt = "Here are some personal memories:\n\n"
        for idx, mem in enumerate(sentimental_memories, 1):
            prompt += f"{idx}. {mem.original}\n"
            prompt += f"   Events: {mem.events}\n"
            prompt += f"   Entities: {mem.entities}\n"
            prompt += f"   Keywords: {mem.keywords}\n"
            prompt += f"   Sentiment: {mem.sentiment} ({mem.sentiment_score:.2f})\n\n"
        return {"message": "LLM prompt prepared", "prompt": prompt}
    except Exception as e:
        logging.error(f"Error in preparing LLM prompt: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Endpoint for LLM story generation
@app.post("/api/llm-process")
async def llm_process(prompt: str):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        full_prompt = f"{prompt}\n\nPlease create a mosaic story or synthesis that weaves together these memories."
        response = model.generate_content(full_prompt)
        return {"message": "Story generated", "story": response.text}
    except Exception as e:
        logging.error(f"Error in LLM processing: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Endpoint for title generation
@app.post("/api/title-generation")
async def title_generation(story: str):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = (
            f"{story}\n\n"
            "Based on the story above, generate a concise, creative title for this memory mosaic. "
            "Respond with only the title, no extra text."
        )
        response = model.generate_content(prompt)
        return {"message": "Title generated", "title": response.text}
    except Exception as e:
        logging.error(f"Error in title generation: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Endpoint for image prompt generation
@app.post("/api/image-prompt")
async def image_prompt(story: str):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = (
            f"{story}\n\n"
            "Based on the story above, create ONE detailed, vivid, and visually clear image prompt for AI image generation. "
            "Respond with only a single image prompt in one complete sentence, describing the scene to be depicted in the image. "
            "Do not include any titles, explanations, or extra text—output only the image prompt."
        )
        response = model.generate_content(prompt)
        return {"message": "Image prompt generated", "image_prompt": response.text}
    except Exception as e:
        logging.error(f"Error in image prompt generation: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Endpoint for image generation
@app.post("/api/generate-image")
async def generate_image_endpoint(image_prompt: str):
    try:
        url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
        headers = {
            "Authorization": f"Bearer {hugging_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json={"inputs": image_prompt})
        if response.ok:
            # Save image temporarily and return base64 or URL for frontend
            img = Image.open(BytesIO(response.content))
            img_path = "generated_image.png"
            img.save(img_path)
            return {"message": "Image generated", "image_path": img_path}
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except Exception as e:
        logging.error(f"Error in image generation: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Endpoint to get all memories
@app.get("/api/memories")
async def get_memories():
    return {"memories": memories}