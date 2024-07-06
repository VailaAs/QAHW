import requests
import pytest


@pytest.fixture()
def url():
    url = 'https://x-clients-be.onrender.com/'
    yield url


class SwaggerApi:
    def __init__(self, url):
        self.url = url

    def company_auth_get_token(self):
        user = "bloom"
        passw = "fire-fairy"
        response = requests.post(f"{self.url}auth/login",
                                json={"username": user, "password": passw})
        token = response.json()["userToken"]
        return token

    def company_create_get_id(self, token):
        my_headers = {'x-client-token': token}
        name = 'test_comp'
        description = 'try out for test'
        response = requests.post(f"{self.url}company", headers=my_headers,
                                json={'name': name, 'description': description})
        company_id = response.json()['id']
        return company_id

    def company_delete(self, token, id):
        my_headers = {'x-client-token': token}
        response = requests.get(f"{self.url}company/delete/{id}",
                                headers=my_headers)
        return response.status_code

    def get_all_employees(self, company_id):
        my_params = {"company": company_id}
        response = requests.get(f"{self.url}employee", params=my_params)
        return response

    def employee_body(self, id, first_name, last_name, middle_name, company_id, email, avatar_url, phone, birthdate):
        body = {
            "id": id,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": company_id,
            "email": email,
            "url": avatar_url,
            "phone": phone,
            "birthdate": f"{birthdate}T00:00:00.000Z",
            "isActive": 'true'
        }
        return body

    def employee_create(self, token, body):
        my_headers = {'x-client-token': token}
        response = requests.post(f"{self.url}employee",
                                 headers=my_headers, json=body)
        employee_id = response.json()['id']
        return employee_id

    def employee_get_by_id(self, employee_id):
        response = requests.get(f"{self.url}employee/{employee_id}")
        return response

    def employee_patch(self, employee_id, token, body):
        my_headers = {'x-client-token': token}
        response = requests.patch(f"{self.url}employee/{employee_id}",
                                  headers=my_headers, json=body)
        return response
