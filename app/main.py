memories = []


text_input = input("text input: ")
print("text: ",text_input)

if text_input.strip():
    memories.append(text_input.strip())



import speech_recognition as sr

def speech_to_text(audio_file=None):
    
    if audio_file is None:
        print("No audio file path provided.")
        return ""
        
    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
            print("recognized text:", text)
            return text
    except Exception as e:
        print("Error:", e)
        return ""





speech_text = speech_to_text("audio.wav")

if speech_text.strip():
    memories.append(speech_text.strip())


import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("gemini_api_key")
genai.configure(api_key=gemini_api_key)

image_path = 'test_image.png'
image = Image.open(image_path)

def image_analysis(image):
    
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = (
            "Analyze the image and generate a detailed, vivid description that captures the visual elements, mood, atmosphere, "
            "and possible stories or emotions present. The description should be rich enough for someone to imagine the scene clearly, "
            "including context, cultural or social significance, and details that might enrich a memory mosaic."
        )
        response = model.generate_content([prompt,image])

        print("Image Analysis: ",response.text)
        return response.text


    except Exception as e:
        print("Error: ",e)
        return ""

    

image_text = image_analysis(image)

if image_text and image_text.strip():
    memories.append(image_text.strip())

print("Memory Array:",memories)

import spacy

nlp = spacy.load("en_core_web_sm")
def nlp_extraction(memories):

    structured = []

    try:
        for mem in memories:
            doc = nlp(mem)
            events = [sent.text for sent in doc.sents]
            entities = [ent.text for ent in doc.ents]
            keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
            structured.append({"original": mem, 
                               "events": events, 
                               "entities": entities, 
                               "keywords": keywords})
        print("NLP Extraction: ",structured)
        return structured
    
    except Exception as e:
        print("Error:",e)
        return ""

structured_text = nlp_extraction(memories)

from transformers import pipeline
import torch


sentimetal_analyzer = pipeline("zero-shot-classification", model="facebook/bart-large-mnli") 


def sentimental_analysis(structured_text):
    for item in structured_text:
        result = sentimetal_analyzer(
            item["original"],
            candidate_labels=["positive", "neutral", "negative"]
        )
        item["sentiment"] = result["labels"][0]
        item["sentiment_score"] = result["scores"][0]
    
    return structured_text


sentimental_text = sentimental_analysis(structured_text)

def prepare_llm_input(sentimental_text):
    prompt = "Here are some personal memories:\n\n"
    for idx, mem in enumerate(sentimental_text, 1):
        prompt += f"{idx}. {mem['original']}\n"
        prompt += f"   Events: {mem.get('events', [])}\n"
        prompt += f"   Entities: {mem.get('entities', [])}\n"
        prompt += f"   Keywords: {mem.get('keywords', [])}\n"
        prompt += f"   Sentiment: {mem.get('sentiment', '')} ({mem.get('sentiment_score', 0):.2f})\n\n"
    return prompt

llm_prompt = prepare_llm_input(sentimental_text)
print("Prompt to send to LLM:\n")
print(llm_prompt)

def llm_process(llm_prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    full_prompt = f"{llm_prompt}\n\nPlease create a mosaic story or synthesis that weaves together these memories."
    response = model.generate_content(full_prompt)
    print("LLM response: ",response.text)
    return response.text


story = llm_process(llm_prompt)

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("gemini_api_key")
genai.configure(api_key=gemini_api_key)

def title_generation(story):
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = (
        f"{story}\n\n"
        "Based on the story above, generate a concise, creative title for this memory mosaic. "
        "Respond with only the title, no extra text."
    )
    response = model.generate_content(prompt)
    print(response.text)
    return response.text
    

title = title_generation(story)

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("gemini_api_key")
genai.configure(api_key=gemini_api_key)

def image_prompt(story):
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = (
        f"{story}\n\n"
        "Based on the story above, create ONE detailed, vivid, and visually clear image prompt for AI image generation. "
        "Respond with only a single image prompt in one complete sentence, describing the scene to be depicted in the image. "
        "Do not include any titles, explanations, or extra text—output only the image prompt."
    )
    response = model.generate_content(prompt)
    print(response.text)
    return response.text

image_prompt = image_prompt(story)

import requests
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()
hugging_token = os.getenv("hugging_face_token")


def generate_image(image_prompt, api_key):
    url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json={"inputs": image_prompt})
    if response.ok:
        img = Image.open(BytesIO(response.content))
        img.show()
        return img
    else:
        print(f"Error {response.status_code}:", response.text)
        return None
image = generate_image(image_prompt, hugging_token)