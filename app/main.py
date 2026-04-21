from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse, Response
from twilio.twiml.messaging_response import MessagingResponse

from .bot import generate_reply
from .config import settings

app = FastAPI(title=settings.app_name)


@app.get("/", response_class=PlainTextResponse)
def root() -> str:
    return "AI WhatsApp Bot is running. POST to /webhook/whatsapp from Twilio Sandbox."


@app.post("/webhook/whatsapp")
def whatsapp_webhook(Body: str = Form(default="")) -> Response:
    bot_response = generate_reply(Body)

    twiml = MessagingResponse()
    twiml.message(bot_response.text)

    return Response(content=str(twiml), media_type="application/xml")
