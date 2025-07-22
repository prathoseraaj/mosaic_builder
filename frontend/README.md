# Memory Mosaic Builder

Memory Mosaic Builder is a full-stack application that allows users to create a "mosaic" of personal memories by combining textual descriptions, audio recordings, and images. The system uses modern NLP and generative AI models to analyze, synthesize, and visualize these memories into a cohesive story and artwork.

## Features

- **Text, Audio, and Image Input:**  
  Users can describe memories via text, upload an audio file for speech-to-text transcription, and/or upload an image for AI-generated scene descriptions.

- **AI-Powered Analysis:**  
  - **NLP Extraction:** Extracts events, entities, and keywords from memory descriptions.
  - **Sentiment Analysis:** Classifies sentiment using zero-shot learning.
  - **Story Synthesis:** Weaves the structured memories into a single narrative using generative AI.
  - **Artwork Generation:** Creates a visual artwork based on the synthesized story using image generation models.

- **Modern Frontend:**  
  Built with React, TypeScript, and Vite for a fast, responsive user interface.

- **Backend API:**  
  FastAPI-based backend orchestrates AI processing, file handling, and serves static/generated assets.

## Directory Structure

```
prathoseraaj-mosaic_builder/
├── requirements.txt
├── app/
│   ├── main.py             
│   └── .gitignore
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   ├── index.css
│   │   └── components/
│   │       ├── Main.tsx
│   │       └── Navbar.tsx
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig*.json
│   └── ...other frontend files
├── notebook/
│   ├── memories_structuring.ipynb
│   └── text_to_speech.ipynb
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/prathoseraaj/mosaic_builder.git
cd prathoseraaj-mosaic_builder
```

### 2. Backend Setup

#### a. Python Environment

- Create a virtual environment and install dependencies:

  ```bash
  python -m venv venv
  source venv/bin/activate 
  pip install -r requirements.txt
  ```

#### b. Environment Variables

- Create a `.env` file in the `app/` directory with your API keys:

  ```
  gemini_api_key=<YOUR_GEMINI_API_KEY>
  hugging_face_token=<YOUR_HUGGINGFACE_TOKEN>
  ```

#### c. Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

#### d. Run the Backend

```bash
cd app
uvicorn main:app --reload
```

The backend will be available at `http://localhost:8000`.

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:5173`.

### 4. Usage

- Open the frontend in your browser.
- Enter a textual description, optionally upload an audio file and/or an image.
- Submit to generate a mosaic story and artwork based on your memory.
- Download or share the generated output as desired.

## API Overview

### POST `/api/memory`

- **Request:**  
  - `description`: Text (required)
  - `audioFile`: File 
  - `imageFile`: File

- **Response:**  
  ```json
  {
    "title": "A Day to Remember",
    "story": "Once upon a time ...",
    "generated_image_url": "/static/memory_xxxxx.png"
  }
  ```

## Notebook Prototypes

- `notebook/memories_structuring.ipynb`: Prototyping for memory structuring, speech-to-text, and image analysis workflows.

## Tech Stack

- **Frontend:** React, TypeScript, Tailwind CSS, Vite
- **Backend:** FastAPI, spaCy, transformers, SpeechRecognition, PIL, Google Generative AI, HuggingFace API
- **Other:** Jupyter Notebook for prototyping



**Disclaimer:** This project uses third-party AI APIs. You are responsible for your API usage and associated costs.
