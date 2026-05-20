import requests
import os
from dotenv import load_dotenv

load_dotenv()


class ApiClient:

    def __init__(self):
        self.base_url = os.getenv("MOCK_API_BASE_URL")

    def fetch_operator_log(self, endpoint: str, entry: str) -> dict:
        """Handles call to log API"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}/{entry.lstrip('/')}"
        response = (requests.get(url, timeout=10))
        response.raise_for_status()
        return response.json()


# client = ApiClient()
# print(client.fetch_operator_log("operator-logs", "LOG-1001"))