# 🌐 Transly AI — ChatGPT-Style Translator

Convert text or voice into 5 supported languages (Hindi, Marathi, Spanish, English, French) with a sleek chat interface.

---

## ⚡ Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ShubhangiWakchaure/Transly_AI_Agent.git
cd Transly_AI_Agent
2️⃣ Create and activate a virtual environment
bash
Copy code
python -m venv venv
Windows

bash
Copy code
venv\Scripts\activate
Mac/Linux

bash
Copy code
source venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Configure the .env file
Create a .env file in the root directory and add:

text
Copy code
GOOGLE_API_KEY=your_api_key_here
Important: Add .env to .gitignore to keep your API key safe.

5️⃣ Run the app
bash
Copy code
python -m app.main
6️⃣ Open in browser
Go to: http://127.0.0.1:7860

🖥 Usage
Type your message in the text box or use the microphone to speak.

Select your target language from the dropdown.

Press the Send button or hit Enter to translate.

The translated response will appear in the chat interface.

🎨 Features
ChatGPT-style conversation interface

Translate text and voice in real-time

Supports 5 languages: Hindi, Marathi, Spanish, English, French

Microphone input for hands-free translation

Sleek, responsive UI with bottom typing panel and language selector

🗂 Folder Structure
text
Copy code
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

⚙️ Technologies Used
Python 3.11+

Gradio (UI & Chatbot)

Google Generative AI (Gemini 1.5)

dotenv (Environment variable management)

🚀 Future Improvements
Public URL deployment

Mobile-friendly responsive UI

More languages and translation engines

Export translations to file

