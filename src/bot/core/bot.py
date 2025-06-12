import discord
from discord.ext import commands
from config.bot_config import BotConfig
from src.bot.core import events
from src.bot.commands import user_commands


def create_bot():
    intents = discord.Intents.default()
    intents.message_content = BotConfig.INTENTS["message_content"]

    bot = commands.Bot(
        command_prefix=BotConfig.PREFIX,
        intents=intents
    )

    # Регистрация событий и команд
    bot.add_listener(on_ready, 'on_ready')
    bot.tree.add_command(user_commands.receiveId)

    return bot


def run_bot():
    bot = create_bot()
    bot.run(BotConfig.TOKEN)