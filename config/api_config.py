import os
from dotenv import load_dotenv

load_dotenv()

class APIConfig:
    BASE_URL = "ttps://api.efezgames.com/v1"#os.getenv("API_BASE_URL")