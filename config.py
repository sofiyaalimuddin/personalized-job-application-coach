import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Retrieve API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

# Gemini model
MODEL = "gemini-3.8-flash"