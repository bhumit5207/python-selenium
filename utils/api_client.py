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
    def put(url: str, body: dict = None, headers: dict = None, timeout: int = 15) -> Response:
        return requests.put(url, json=body, headers=headers, timeout=timeout)

    @staticmethod
    def patch(url: str, body: dict = None, headers: dict = None, timeout: int = 15) -> Response:
        return requests.patch(url, json=body, headers=headers, timeout=timeout)

    @staticmethod
    def delete(url: str, headers: dict = None, timeout: int = 15) -> Response:
        return requests.delete(url, headers=headers, timeout=timeout)

    @staticmethod
    def assert_status(response: Response, expected_code: int = 200):
        if response.status_code != expected_code:
            raise AssertionError(f'Expected {expected_code} but got {response.status_code}. Body: {response.text}')

    @staticmethod
    def assert_content_type(response: Response, expected_type: str = 'application/json'):
        content_type = response.headers.get('Content-Type', '')
        if expected_type not in content_type:
            raise AssertionError(f'Expected Content-Type to include "{expected_type}" but got "{content_type}"')

    @staticmethod
    def assert_json_keys(json_data: dict, required_keys: list):
        missing = [key for key in required_keys if key not in json_data]
        if missing:
            raise AssertionError(f'Missing expected JSON keys: {missing}. Actual keys: {list(json_data.keys())}')
