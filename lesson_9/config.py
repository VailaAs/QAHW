import pytest, requests

@pytest.fixture()
def token(url):
    user = "bloom"
    passw = "fire-fairy"
    response = requests.post(url + 'auth/login',
                                json={"username": user, "password": passw})
    token = response.json()["userToken"]
    return token
