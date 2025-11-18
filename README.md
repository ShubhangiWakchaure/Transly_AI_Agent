Transly AI — Language Translator
Transly AI is a modern AI-powered translator with a ChatGPT-style interface. It allows users to translate text and speech into 5 supported languages in real-time.

This project combines Google Generative AI, speech-to-text, and Gradio to create an interactive and stylish translation interface.

🎯 Features

Translate text or voice input into:

Hindi 🇮🇳

Marathi 🇮🇳

Spanish 🇪🇸

English 🇬🇧

French 🇫🇷

Chat-style interface inspired by ChatGPT

Voice input support with microphone button

Responsive design with typing panel at bottom

Language selection dropdown with icons for clarity

Lightweight and runs locally using Python & Gradio

💻 Demo Preview

<!-- Optional: screenshot -->

🛠️ Technologies Used

Python 3.10+

Google Generative AI (Gemini 1.5 model)

Gradio (UI & Chat Interface)

SpeechRecognition & pydub (for audio to text)

dotenv (for safe API key management)

📁 Project Structure
Transly_AI_Agent/
│
├─ app/
│   ├─ main.py           # Entry point of the app
│   ├─ translator.py     # Translation logic with AI model
│   ├─ speech_to_text.py # Voice-to-text processing
│   ├─ ui.py             # Gradio UI components & styling
│   └─ languages.py      # Language codes mapping
│
├─ .env                  # API keys (ignored in GitHub)
├─ requirements.txt      # Python dependencies
├─ README.md
└─ assets/               # Optional images for README/UI

⚡ Quick Start
1. Clone the repository
git clone https://github.com/your-username/Transly_AI_Agent.git
cd Transly_AI_Agent

2. Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Add your .env file
GOOGLE_API_KEY=your_api_key_here


Important: .env is ignored in GitHub for security.

5. Run the app
python -m app.main


Open your browser and go to: http://127.0.0.1:7860

🖌️ UI Design

Left-hand side: Language selection dropdown with icons

Main section: Chat messages with user and AI messages

Bottom: Typing panel + microphone + send button

Clean, minimalistic, and responsive