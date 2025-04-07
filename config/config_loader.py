import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "prod")

CONFIG = {
    "prod": {
        "BASE_URL": "https://poetrydb.org",
        "MOCK_API_URL": "https://jsonplaceholder.typicode.com"
    },
    "dev": {
        "BASE_URL": "https://dev.poetrydb.org",
        "MOCK_API_URL": "https://jsonplaceholder.typicode.com"
    },
    "stg": {
        "BASE_URL": "https://stg.poetrydb.org",
        "MOCK_API_URL": "https://jsonplaceholder.typicode.com"
    },
    "local": {
        "BASE_URL": "http://localhost:8000",
        "MOCK_API_URL": "http://localhost:8001"
    }
    # Add more environments as needed
    # "test": {
    #     "BASE_URL": "https://test.poetrydb.org",
    #     "MOCK_API_URL": "https://jsonplaceholder.typicode.com"
    # }
}

ENV_CONFIG = CONFIG.get(ENV, CONFIG["prod"])
