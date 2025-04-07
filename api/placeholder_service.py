import requests
from config.config_loader import ENV_CONFIG

def get_random_user():
    url = f"{ENV_CONFIG['MOCK_API_URL']}/users"
    response = requests.get(url)
    response.raise_for_status()

    users = response.json()
    if not users:
        raise Exception("No users returned from API")

    return users[0]  # return the first user

def create_post_for_user(user_id: int, title="Test Post", body="This is a post created during test"):
    url = f"{ENV_CONFIG['MOCK_API_URL']}/posts"
    payload = {
        "userId": user_id,
        "title": title,
        "body": body
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()
