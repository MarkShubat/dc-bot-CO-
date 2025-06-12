import os
from dotenv import load_dotenv

load_dotenv()

class BotConfig:
    PREFIX = "/"
    TOKEN = os.getenv("DISCORD_TOKEN")
    INTENTS = {"message_content": True}