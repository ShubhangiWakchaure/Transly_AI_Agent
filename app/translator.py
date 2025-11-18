import os
from google.genai import Client
from app.languages import LANG_CODES
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

client = Client(api_key=API_KEY)

MODEL_NAME = "gemini-2.5-flash"  # Use a valid model you have access to

def translate_text(text: str, language: str) -> str:
    lang_code = LANG_CODES.get(language, "en")
    contents = f"Translate the following to {language} (code {lang_code}):\n{text}"

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
