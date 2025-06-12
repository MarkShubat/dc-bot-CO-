from discord.ext import commands

async def on_ready(bot: commands.Bot):
    print(f'✅ Бот {bot.user} в сети!')
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Синхронизировано {len(synced)} команд(ы)")
    except Exception as e:
        print(f"Ошибка при синхронизации команд: {e}")