import requests
from requests import Response


class APIClient:
    @staticmethod
    def get(url: str, params: dict = None, headers: dict = None, timeout: int = 15) -> Response:
        return requests.get(url, params=params, headers=headers, timeout=timeout)

    @staticmethod
    def post(url: str, body: dict = None, headers: dict = None, timeout: int = 15) -> Response:
        return requests.post(url, json=body, headers=headers, timeout=timeout)

    @staticmethod
    def assert_status(response: Response, expected_code: int = 200):
        if response.status_code != expected_code:
            raise AssertionError(f'Expected {expected_code} but got {response.status_code}. Body: {response.text}')
