# AI WhatsApp Bot

I made this project because I thought it would be really fun to connect AI to something as familiar and everyday as WhatsApp. I wanted to go beyond a simple chatbot running in a notebook and build something that could actually receive a message, process it, and reply like a tiny AI assistant inside a real chat app.

This project gave me a chance to experiment with conversational AI, webhooks, backend development, and model integration in one small end-to-end system. I was especially interested in seeing how tools like **FastAPI**, **Twilio WhatsApp Sandbox**, and lightweight local language models could work together to create a practical prototype.

The result is a simple WhatsApp chatbot starter that receives incoming messages through a webhook, generates a reply using a local AI model or fallback logic, and sends the response back to the user.

More than anything, this project was a fun build — part AI experiment, part software engineering project, and a good way to turn curiosity into something tangible.

## Features

- WhatsApp webhook using Twilio Sandbox
- FastAPI backend
- Local AI response engine with Hugging Face `transformers`
- Environment-variable based config
- Clean project structure
- Easy to extend with memory, database, or custom intent handling

## Project Structure

```text
ai-whatsapp-bot/
├── app/
│   ├── main.py
│   ├── bot.py
│   ├── config.py
│   └── prompts.py
├── tests/
│   └── test_bot.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## How It Works

1. A user sends a WhatsApp message to your Twilio sandbox number.
2. Twilio sends the incoming message to your FastAPI webhook.
3. The app generates a response using a small conversational model.
4. The app returns TwiML, and Twilio sends the reply back to WhatsApp.

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ai-whatsapp-bot.git
cd ai-whatsapp-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create environment file

```bash
cp .env.example .env
```

### 5. Run the app

```bash
uvicorn app.main:app --reload
```

The webhook will run locally at:

```text
http://127.0.0.1:8000/webhook/whatsapp
```

### 6. Expose it publicly

Use ngrok:

```bash
ngrok http 8000
```

Copy the generated HTTPS URL and set your Twilio WhatsApp sandbox webhook to:

```text
https://your-ngrok-url/webhook/whatsapp
```

## Twilio Setup

1. Create a Twilio account.
2. Open the WhatsApp Sandbox.
3. Join the sandbox from your phone using the provided code.
4. In Sandbox settings, set the incoming webhook URL to your public ngrok URL.

## Environment Variables

See `.env.example`.

## Notes

- The default model used here is `microsoft/DialoGPT-small`.
- The first run may take time because the model downloads locally.
- If model loading fails, the app falls back to a rule-based reply so the demo still works.

## Future Improvements

- Add chat memory with SQLite or Redis
- Add user profiles and conversation context
- Add intent detection and command routing
- Connect to a custom fine-tuned model
- Deploy on Render, Railway, or a VPS


