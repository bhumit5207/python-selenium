from utils.api_client import APIClient
from utils.data_reader import DataReader


def test_api_get_request():
    """Send a GET request to the sample API and verify the status code and JSON payload."""
    data = DataReader.read_json('data/test_data.json')['api']
    url = f"{data['base_url']}{data['resource']}"
    response = APIClient.get(url)
    APIClient.assert_status(response, 200)
    json_data = response.json()
    assert json_data['id'] == 1
    assert 'userId' in json_data
