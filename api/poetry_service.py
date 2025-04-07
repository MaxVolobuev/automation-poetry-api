import requests
from config.config_loader import ENV_CONFIG

def get_poems_by_author(author: str):
    url = f"{ENV_CONFIG['BASE_URL']}/author/{author}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def search_poems_by_word(word: str):
    url = f"{ENV_CONFIG['BASE_URL']}/lines/{word}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
