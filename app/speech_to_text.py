import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def audio_to_text(filepath):
    """Convert user's microphone speech to text"""

    try:
        with open(filepath, "rb") as f:
            audio_data = f.read()

        resp = model.generate_content([
            "Transcribe the audio to text:",
            {"mime_type": "audio/wav", "data": audio_data}
        ])

        return resp.text

    except Exception as e:
        return f"Error converting speech: {str(e)}"
