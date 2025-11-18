# 🌐 Transly AI — Language Translator

**Transly AI** is a desktop/web-based AI-powered translator that allows you to convert text or voice into **5 supported languages**: Hindi, Marathi, Spanish, English, and French. The app features a modern chat interface with a typing panel, microphone input, and send button.

---

## 🛠 Features

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

2️⃣ Create and activate a virtual environment

python -m venv venv


Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Configure the .env file
Create a .env file in the root directory and add:

GOOGLE_API_KEY=your_api_key_here


Make sure .env is added to .gitignore to keep your API key safe.

5️⃣ Run the app

python -m app.main


6️⃣ Open in browser: http://127.0.0.1:7860

🖥 Usage

Type your message in the text box or use the microphone to speak.

Select your target language from the dropdown.

Press the Send button or hit Enter to translate.

The translated response will appear in the chat interface.

