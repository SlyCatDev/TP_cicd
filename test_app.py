import requests

def test_users():
    response = requests.get("http://localhost:5001/users")
    assert response.status_code == 200