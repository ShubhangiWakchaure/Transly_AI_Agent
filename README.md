# 🌐 Transly AI — ChatGPT-Style Translator

**Transly AI** is a desktop/web-based AI-powered translator that allows you to convert text or voice into **5 supported languages**: Hindi, Marathi, Spanish, English, and French. The app features a modern chat interface with a typing panel, microphone input, and send button.

---

## 🛠 Features

- ChatGPT-style conversational UI
- Translate **text and voice** into multiple languages
- Voice input via microphone
- Language selection dropdown with icons
- Modern, sleek design using **Gradio**
- Works locally and can be deployed publicly

---

## ⚡ Quick Start

1️⃣ **Clone the repository and navigate into it**  
```bash
git clone https://github.com/ShubhangiWakchaure/Transly_AI_Agent.git
cd Transly_AI_Agent

```
2️⃣ **Create and activate a virtual environment**
```bash
python -m venv venv

Windows 
 venv\Scripts\activate
Mac/Linux

source venv/bin/activate

```
3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt


```
4️⃣ **Run the app**
```bash
python -m app.main

```
5️⃣ **Open in browser**

Go to: http://127.0.0.1:7860

---

## 🖥 Usage

- Type your message in the text box or use the microphone to speak.

- Select your target language from the dropdown.

- Press the Send button or hit Enter to translate.

- The translated response will appear in the chat interface.

---
``
### 🗂 Folder Structure

Transly_AI_Agent/
│
├─ app/
│  ├─ main.py           # Main app launcher
│  ├─ ui.py             # Gradio UI components
│  ├─ translator.py     # Google Gemini translation logic
│  └─ languages.py      # Language code mapping
│
├─ .env                 # API key (ignored in git)
├─ requirements.txt     # Python dependencies
└─ README.md            # Project documentation 

---
``
## ⚙️ Technologies Used

- Python 3.11+

- Gradio (UI & Chatbot)

- Google Generative AI (Gemini 1.5)

- dotenv (Environment variable management)