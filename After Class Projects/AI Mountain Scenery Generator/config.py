import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY", "")
HF_MODEL = os.getenv("HF_MODEL", "black-forest-labs/FLUX.1-schnell")

APP_TITLE = "AI Mountain Scenery Generator"
APP_SUBTITLE = (
    "Create beautiful landscape images by choosing mountain type, weather, "
    "time of day, mood, and style."
)

MOUNTAIN_TYPES = [
    "Snowy Alps",
    "Rocky Peaks",
    "Volcanic Mountains",
    "Forest Mountains",
    "Desert Cliffs",
    "Fantasy Floating Mountains",
]

WEATHER_OPTIONS = [
    "Clear sky",
    "Cloudy",
    "Foggy",
    "Rainy",
    "Snowy",
    "Stormy",
]

TIME_OF_DAY_OPTIONS = [
    "Sunrise",
    "Morning",
    "Golden hour",
    "Sunset",
    "Twilight",
    "Night",
]

MOOD_OPTIONS = [
    "Peaceful",
    "Epic",
    "Dreamy",
    "Mystical",
    "Adventurous",
    "Calm",
]

STYLE_OPTIONS = [
    "Realistic",
    "Digital painting",
    "Fantasy art",
    "Watercolor",
    "Cinematic concept art",
]

NEGATIVE_PROMPT = (
    "blurry, low quality, distorted, deformed, extra objects, people, text, watermark"
)