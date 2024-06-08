import requests
import pytest


@pytest.fixture()
def url():
    url = 'https://x-clients-be.onrender.com/'
    yield url


class CompanyApi:

    def __init__(self, url):
        self.url = url
  
# auth company
    def company_auth(self):
        user = "dude"
        password = "cool"
        response = requests.post(f"{self.url}auth/login", json={"username": user, "password": password})
        return response


# check with user and pass
#check only user
#check only pass
#check empty body

