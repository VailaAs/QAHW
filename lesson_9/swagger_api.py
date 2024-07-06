import requests
from config import *


class SwaggerApi:
    def __init__(self, url):
        self.url = url

    def company_create_get_id(self, token:str, name:str, description:str):
        my_headers = {'x-client-token': token}
        response = requests.post(self.url + "company", headers=my_headers,
                                json={'name': name, 'description': description})
        company_id = response.json()['id']
        return company_id
    
    def get_last_created_company(self):
        my_params = {"isActive": True}
        response = requests.get(self.url + "company", params=my_params)
        return response.json()[-1]

    def company_delete(self, token:str, id:int):
        my_headers = {'x-client-token': token}
        response = requests.get(self.url + "company/delete/" + id,
                                headers=my_headers)
        return response.status_code

    def get_all_employees(self, company_id:int):
        my_params = {"company": company_id}
        response = requests.get(self.url + "employee", params=my_params)
        return response.json()

    def employee_body(self, id:int, first_name:str, last_name:str, company_id:int, phone:str):
        body = {
            "id": id,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": "",
            "companyId": company_id,
            "email": "",
            "url": "",
            "phone": phone,
            "birthdate": "",
            "isActive": 'true'
        }
        return body

    def employee_create(self, token:str, body:dict):
        my_headers = {'x-client-token': token}
        response = requests.post(self.url + "employee",
                                 headers=my_headers, json=body)
        employee_id = response.json()['id']
        return employee_id

    def employee_get_by_id(self, employee_id:int):
        response = requests.get(self.url + "employee/" + str(employee_id))
        return response

    def employee_patch(self, employee_id:int, token:str, body:dict):
        my_headers = {'x-client-token': token}
        response = requests.patch(self.url + "employee/" + str(employee_id),
                                  headers=my_headers, json=body)
        return response
