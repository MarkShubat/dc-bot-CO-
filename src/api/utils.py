import re
import base64

def encode_nickname(nickname: str) -> str:
    """Обрабатывает никнейм для API запроса"""
    def has_russian_letters(string):
        return bool(re.search('[а-яА-Я]', string))

    if nickname.startswith("#"):
        first = int(nickname[1:3], 16)
        second = int(nickname[3:5], 16)
        third = int(nickname[5:], 16)
        return f"ID={first * 256 * 256 + second * 256 + third}"
    elif has_russian_letters(nickname):
        encoded = base64.b64encode(nickname.encode('utf-8')).decode('utf-8')
        return f"nick=@{encoded}"
    else:
        return f"nick={nickname}"