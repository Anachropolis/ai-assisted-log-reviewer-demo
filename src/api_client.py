import requests
import os
from dotenv import load_dotenv

load_dotenv()


class ApiClient:

    def __init__(self):
        self.base_url = os.getenv("MOCK_API_BASE_URL", "http://127.0.0.1:8000")

    def fetch_operator_log(self, endpoint: str, entry: str) -> dict:
        """Fetch one operator log from API endpoint"""
        url = f"{self.base_url}/{endpoint.strip('/')}/{entry.strip('/')}"
        response = (requests.get(url, timeout=10))
        response.raise_for_status()
        return response.json()

    def fetch_log_list(self, endpoint: str) -> dict:
        """Fetch all logs from API endpoint"""
        url = f"{self.base_url}/{endpoint.strip('/')}"
        response = (requests.get(url, timeout=10))
        return response.json()

