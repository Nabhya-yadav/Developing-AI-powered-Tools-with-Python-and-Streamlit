# In Python, config.py is a naming convention for a Python file used to store global configuration settings, environment variables, and constants for an application.

# pip install python-dotenv
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY", "")
# You can change this model later if needed
HF_IMAGE_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"
HF_IMAGE_API_URL = f"https://api-inference.huggingface.co/models/{HF_IMAGE_MODEL}"