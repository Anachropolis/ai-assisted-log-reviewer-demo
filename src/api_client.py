import requests


class ApiClient:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"

    def fetch_operator_log(self, endpoint: str, entry: str) -> dict:

        url = f"{self.base_url}/{endpoint.lstrip('/')}/{entry.lstrip('/')}"
        response = (requests.get(url, timeout=10))
        response.raise_for_status()
        return response.json()


# client = ApiClient()
# print(client.fetch_operator_log("operator-logs", "LOG-1001"))