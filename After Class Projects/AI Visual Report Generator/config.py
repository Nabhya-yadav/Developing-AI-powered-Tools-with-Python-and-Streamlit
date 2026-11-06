import os
from dotenv import load_dotenv

load_dotenv()

APP_TITLE = "AI Visual Report Generator"
APP_SUBTITLE = (
    "Upload an image and generate a structured visual + text report with overlays, "
    "parsed JSON, and summary sections."
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
MODEL_NAME = os.getenv("GROQ_MODEL", "meta-llama/llama-4-scout-17b-16e-instruct")

SYSTEM_PROMPT = (
    "You are a careful visual analysis assistant. "
    "Be responsible: do not identify real people, do not make sensitive guesses, "
    "and only describe what is visible or strongly implied."
)

USER_PROMPT = '''
Analyze the uploaded image and return ONLY valid JSON in this exact structure:

{
  "scene_type": "short phrase",
  "mood": "short phrase",
  "safety_note": "one sentence about uncertainty and responsible interpretation",
  "objects": [
    {
      "label": "object name",
      "confidence": "high/medium/low",
      "reason": "very short reason",
      "box": {
        "x1": 0.10,
        "y1": 0.15,
        "x2": 0.40,
        "y2": 0.55
      }
    }
  ]
}

Rules:
- Use 3 to 6 major objects if possible.
- Coordinates must be normalized between 0 and 1.
- Do not include markdown.
- Do not include any text outside JSON.
'''