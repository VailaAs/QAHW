import requests
import pytest


@pytest.fixture()
def url():
    url = 'https://todo-app-sky.herokuapp.com/'
    yield url


class ToDoList:
    def __init__(self, url):
        self.url = url

    def task_create(self, task_name:str):
        response = requests.post(self.url,
                                json={"title": task_name, "completed": False})
        return response

    def task_edit(self, task_id: int, new_task_name:str):
        response = requests.patch(f"{self.url}/{task_id}", json={"title": new_task_name})
        return response

    def task_delete(self, task_id: int):
        response = requests.delete(f"{self.url}/{task_id}")
        return response

    def get_task_list(self):
        response = requests.get(self.url)
        return response

    def get_task(self, task_id):
        response = requests.get(f"{self.url}/{task_id}")
        return response

    def task_mark_completed(self, task_id):
        response = requests.patch(f"{self.url}/{task_id}", json={"completed":True})
        return response

    def task_mark_uncompleted(self, task_id):
        response = requests.patch(f"{self.url}/{task_id}", json={"completed":False})
        return response
