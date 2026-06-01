from utils.api_client import APIClient
from utils.data_reader import DataReader


def test_api_get_request():
    """Send a GET request to the sample API and verify the status code and JSON payload."""
    data = DataReader.read_json('data/test_data.json')['api']
    url = f"{data['base_url']}{data['resource']}"
    response = APIClient.get(url)

    APIClient.assert_status(response, 200)
    APIClient.assert_content_type(response, 'application/json')

    json_data = response.json()
    APIClient.assert_json_keys(json_data, ['userId', 'id', 'title', 'body'])
    assert json_data['id'] == 1
    assert isinstance(json_data['userId'], int)
    assert isinstance(json_data['title'], str)
    assert isinstance(json_data['body'], str)


def test_api_create_resource():
    """Send a POST request to create a resource and validate the returned JSON response."""
    data = DataReader.read_json('data/test_data.json')['api']
    url = f"{data['base_url']}/posts"
    payload = {
        'title': 'Full API validation test',
        'body': 'This request verifies POST behavior and response schema.',
        'userId': 123
    }

    response = APIClient.post(url, body=payload)
    APIClient.assert_status(response, 201)
    APIClient.assert_content_type(response, 'application/json')

    json_data = response.json()
    APIClient.assert_json_keys(json_data, ['id', 'title', 'body', 'userId'])
    assert json_data['title'] == payload['title']
    assert json_data['body'] == payload['body']
    assert json_data['userId'] == payload['userId']
    assert isinstance(json_data['id'], int)


def test_api_update_resource_put():
    """Send a PUT request to update a resource and validate the returned JSON response."""
    data = DataReader.read_json('data/test_data.json')['api']
    url = f"{data['base_url']}{data['resource']}"
    payload = {
        'id': 1,
        'title': 'Updated title via PUT',
        'body': 'PUT request updated the body content.',
        'userId': 123
    }

    response = APIClient.put(url, body=payload)
    APIClient.assert_status(response, 200)
    APIClient.assert_content_type(response, 'application/json')

    json_data = response.json()
    APIClient.assert_json_keys(json_data, ['userId', 'id', 'title', 'body'])
    assert json_data['title'] == payload['title']
    assert json_data['body'] == payload['body']
    assert json_data['userId'] == payload['userId']
    assert json_data['id'] == payload['id']


def test_api_update_resource_patch():
    """Send a PATCH request to partially update a resource and validate the returned JSON response."""
    data = DataReader.read_json('data/test_data.json')['api']
    url = f"{data['base_url']}{data['resource']}"
    payload = {
        'title': 'Patched title',
        'body': 'PATCH request changed only the title and body.'
    }

    response = APIClient.patch(url, body=payload)
    APIClient.assert_status(response, 200)
    APIClient.assert_content_type(response, 'application/json')

    json_data = response.json()
    APIClient.assert_json_keys(json_data, ['userId', 'id', 'title', 'body'])
    assert json_data['title'] == payload['title']
    assert json_data['body'] == payload['body']


def test_api_delete_resource():
    """Send a DELETE request to remove a resource and validate the response."""
    data = DataReader.read_json('data/test_data.json')['api']
    url = f"{data['base_url']}{data['resource']}"

    response = APIClient.delete(url)
    APIClient.assert_status(response, 200)
    assert response.text == '{}' or response.text == ''
