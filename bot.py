import requests
import re
import base64
import json
from discord.ext import commands
import nest_asyncio
import asyncio

def getId(nick):
    def has_russian_letters(string):
        pattern = re.compile('[а-яА-Я]')
        return re.search(pattern, string) is not None

    if nick[0] == "#":
        first = int(nick[1:3], 16)
        second = int(nick[3:5], 16)
        third = int(nick[5:], 16)
        nick = str(first * 256 * 256 + second * 256 + third)
        nick = "ID=" + nick
    elif has_russian_letters(nick):
        nick = base64.b64encode(nick.encode('utf-8'))
        nick = str(nick)[2:len(str(nick)) - 1]
        nick = "@" + str(nick)
        nick = "nick=" + nick
    else:
        nick = "nick=" + nick

    req1 = "https://api.efezgames.com/v1/social/findUser?{NICK}"
    request1 = req1.format(NICK=nick)
    response = requests.get(request1)
    try:
        data = json.loads(response.text)
        uID = str(data["_id"])
    except json.decoder.JSONDecodeError:
        return "error"
    return uID

# Применяем патч для работы с event loop в Jupyter
nest_asyncio.apply()

# Создаем объект интентов
intents = discord.Intents.default()
intents.message_content = True  # Включаем доступ к содержимому сообщений (если нужно)

# Создаем экземпляр бота
bot = commands.Bot(command_prefix="/", intents=intents)

# Событие при запуске бота
@bot.event
async def on_ready():
    print(f'✅ Бот {bot.user} в сети!')
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Синхронизировано {len(synced)} команд(ы)")
    except Exception as e:
        print(f"Ошибка при синхронизации команд: {e}")

@bot.tree.command(name="receive-id", description="Get Case Opener ID")
async def receiveId(interaction: discord.Interaction, nickname: str):
    id = getId(nickname)
    await interaction.response.send_message(f"Your Id: **{id}**")

# Асинхронный запуск бота
async def main():
    async with bot:
        await bot.start("MTM4MTY4NjYyMjc2ODA3NDc2Mg.GQve3B.kpxIUU8h-vTn3qOz2hwBXsjcoJKlnTaM_H7pYU")  # Замените на ваш токен

# Запускаем бота
await main()
