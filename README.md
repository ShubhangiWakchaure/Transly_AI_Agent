# 🌐 Transly AI — Language Translator

![Transly AI](assets/cover.png) <!-- optional banner image -->

**Transly AI** is an AI powered Interface like **Gemini**. Convert text or voice into **five supported languages** with a clean, interactive chat interface.  

---

## 🚀 Features

- Translate **text and speech** in real-time
- Supported languages: **Hindi**, **Marathi**, **Spanish**, **English**, **French**
- Modern **chat-style interface** with user and AI messages
- **Microphone input** for voice-to-text translation
- **Language selection dropdown** with icons
- Responsive, minimalistic UI  

---

## 💻 Technologies Used

- Python 3.10+  
- [Google Generative AI (Gemini 1.5 model)](https://developers.generativeai.google/) for translation  
- [Gradio](https://gradio.app/) for chat interface  
- **SpeechRecognition** and **pydub** for audio processing  
- **dotenv** for secure API key management  

---

## 📂 Project Structure

Transly_AI_Agent/
│
├─ app/
│ ├─ main.py # Entry point of the app
│ ├─ translator.py # AI translation logic
│ ├─ speech_to_text.py # Audio-to-text logic
│ ├─ ui.py # Gradio UI layout & styling
│ └─ languages.py # Language code mapping
│
├─ assets/ # Images/screenshots for README
├─ .env # Environment variables (ignored in Git)
├─ requirements.txt # Python dependencies
└─ README.md

---

## ⚡ Quick Start

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ShubhangiWakchaure/Transly_AI_Agent.git
cd Transly_AI_Agent

---
2️⃣ Create and activate virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

---

3️⃣ Install dependencies

pip install -r requirements.txt

---

4️⃣ Configure .env file

Create a .env file in the root directory:

GOOGLE_API_KEY=your_api_key_here

---

5️⃣ Run the app
python -m app.main

Open in browser: http://127.0.0.1:7860

---

