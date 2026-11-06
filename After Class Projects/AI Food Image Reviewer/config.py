import os
from dotenv import load_dotenv

load_dotenv()

APP_TITLE = "AI Food Image Reviewer"
APP_SUBTITLE = (
    "Upload a food image, choose a review style, and let Groq Vision generate "
    "a structured food review."
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
MODEL_NAME = os.getenv("GROQ_MODEL", "meta-llama/llama-4-scout-17b-16e-instruct")

STYLES = {
    "Funny": (
        "Write a light, playful food review. Keep it fun but still describe the dish clearly."
    ),
    "Critic": (
        "Write like a food critic with observation, presentation, texture, and appeal."
    ),
    "Health": (
        "Write a healthy-eating focused review, commenting on ingredients, balance, and overall impression."
    ),
}

def build_prompt(style_key: str) -> str:
    style_instruction = STYLES.get(style_key, STYLES["Funny"])
    return (
        "Look carefully at the uploaded food image and generate a structured review using this format:"
        "Dish guess:"

        "Visual appeal:"

        "Ingredients you can identify:"

        "Texture or freshness clues:"

        "Style review:"

        "Overall verdict:"


        f"Style instruction: {style_instruction} "
        "Only mention what is visible or strongly implied from the image."
    )