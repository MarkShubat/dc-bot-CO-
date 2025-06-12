import discord
from discord import app_commands
from discord.ext import commands
from src.api.client import APIClient
from src.utils.errors import APIError

class UserCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.api = APIClient()

    @app_commands.command(name="receive-id", description="Get Case Opener ID")
    async def receiveId(self, interaction: discord.Interaction, nickname: str):
        try:
            user_id = self.api.get_user_id(nickname)
            await interaction.response.send_message(f"Your Id: **{user_id}**")
        except APIError as e:
            await interaction.response.send_message(f"❌ Error: {e.message}")

async def setup(bot: commands.Bot):
    await bot.add_cog(UserCommands(bot))