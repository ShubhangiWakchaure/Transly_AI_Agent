import gradio as gr
from app.translator import translate_text
from app.languages import LANG_CODES
import base64

SUPPORTED_LANGUAGES = ["Hindi", "Marathi", "Spanish", "English", "French"]

# Load the uploaded logo as base64
def get_logo_base64(path="assests\logo.png"):
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:image/png;base64,{encoded}"

def build_interface():
    logo_src = get_logo_base64()

    with gr.Blocks(css="""
        .header {text-align: center; margin-bottom: 10px;}
        .chat-container {height: 400px; overflow-y: auto; padding: 10px; border-radius: 15px; background-color: #f5f5f5;}
        .message-user {background-color: #DCF8C6; border-radius: 12px; padding: 8px; margin: 5px; max-width: 70%; align-self: flex-end;}
        .message-bot {background-color: #ffffff; border-radius: 12px; padding: 8px; margin: 5px; max-width: 70%; align-self: flex-start;}
        .input-panel {display: flex; gap: 10px; padding: 5px; margin-top: 5px;}
        .send-btn {background-color: #4CAF50; color: white; border-radius: 12px; padding: 10px 15px;}
        .mic-btn {background-color: #2196F3; color: white; border-radius: 12px; padding: 10px;}
        .lang-dropdown {border-radius: 12px; padding: 5px; margin-bottom: 10px;}
    """) as demo:

        # Header with logo
        gr.Markdown(f"""
<div class="header">
    <img src="{logo_src}" width="50" style="vertical-align: middle; margin-right:10px;">
    <span style="font-size:30px; font-weight:bold;">Transly AI — Translator</span>
</div>
""")

        # Language selector below header
        lang_selector = gr.Dropdown(
            SUPPORTED_LANGUAGES,
            label="🌍 Select Language",
            value="English",
            elem_classes="lang-dropdown"
        )

        # Chatbot area
        chatbot = gr.Chatbot(elem_classes="chat-container", height=400, type="messages")

        # Input row
        with gr.Row(elem_classes="input-panel"):
            user_input = gr.Textbox(
                placeholder="Type a message...",
                show_label=False
            )
            mic = gr.Audio(sources=["microphone"], type="filepath", label=None, elem_classes="mic-btn")
            send_btn = gr.Button("➤", elem_classes="send-btn")

        # Backend logic
        def process_message(message, history, target_lang):
            if not message:
                return history
            translated = translate_text(message, target_lang)
            history.append({"role": "user", "content": message})
            history.append({"role": "assistant", "content": translated})
            return history

        send_btn.click(
            process_message,
            inputs=[user_input, chatbot, lang_selector],
            outputs=chatbot
        )

        user_input.submit(
            process_message,
            inputs=[user_input, chatbot, lang_selector],
            outputs=chatbot
        )

    return demo
