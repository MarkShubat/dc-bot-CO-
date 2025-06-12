import requests
import json
from config.api_config import APIConfig
from src.api.utils import encode_nickname
from src.utils.errors import APIError


class APIClient:
    def __init__(self):
        self.base_url = APIConfig.BASE_URL

    def get_user_id(self, nickname: str) -> str:
        """Получает ID пользователя по никнейму"""
        processed_nick = encode_nickname(nickname)
        url = f"{self.base_url}/social/findUser?{processed_nick}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return str(data["_id"])
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            raise APIError(f"Failed to get user ID: {str(e)}")