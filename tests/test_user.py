import requests
import pytest

def test_unauthorized_access(mocker):
    url = "http://127.0.0.1:8000"
    params = {"username": "admin", "password": "admin"}
    
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""
    
    mocker.patch("requests.get", return_value=mock_response)
    response = requests.get(url, params=params)
    
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    assert isinstance(response.text, str), "Expected text response"
    assert response.text == "", f"Expected empty response, got: {response.text}"

def test_authorized_access(mocker):
    url = "http://127.0.0.1:8000"
    params = {"username": "admin", "password": "qwerty"}
    
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""
    
    mocker.patch("requests.get", return_value=mock_response)
    response = requests.get(url, params=params)
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert isinstance(response.text, str), "Expected text response"
    assert response.text == "", f"Expected empty response, got: {response.text}"
