from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Optional

from .config import settings
from .prompts import SYSTEM_STYLE


@dataclass
class BotResponse:
    text: str
    source: str


class RuleBasedFallback:
    def generate(self, user_message: str) -> BotResponse:
        text = user_message.strip().lower()
        if not text:
            return BotResponse("Hi! Send me a message and I'll reply.", "fallback")
        if "hello" in text or "hi" in text:
            return BotResponse("Hey! How can I help you today?", "fallback")
        if "resume" in text:
            return BotResponse("I can help you draft project bullets, summaries, or interview answers.", "fallback")
        if "project" in text:
            return BotResponse("This bot can be extended to answer questions about projects, reminders, or FAQs.", "fallback")
        return BotResponse(f"You said: {user_message}. I'm a starter AI bot, but you can extend me with memory and custom features.", "fallback")


class LocalDialoGPT:
    def __init__(self) -> None:
        from transformers import AutoModelForCausalLM, AutoTokenizer
        import torch

        self.torch = torch
        self.tokenizer = AutoTokenizer.from_pretrained(settings.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(settings.model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate(self, user_message: str) -> BotResponse:
        prompt = f"{SYSTEM_STYLE}\nUser: {user_message}\nAssistant:"
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        output = self.model.generate(
            **inputs,
            max_new_tokens=settings.max_new_tokens,
            temperature=settings.temperature,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id,
        )
        decoded = self.tokenizer.decode(output[0], skip_special_tokens=True)
        reply = decoded.split("Assistant:")[-1].strip()
        reply = reply.split("User:")[0].strip()
        if not reply:
            reply = "I'm here. Tell me what you'd like help with."
        return BotResponse(reply, "dialoGPT")


@lru_cache(maxsize=1)
def get_bot_engine() -> object:
    try:
        return LocalDialoGPT()
    except Exception:
        return RuleBasedFallback()


def generate_reply(user_message: str) -> BotResponse:
    engine = get_bot_engine()
    return engine.generate(user_message)
