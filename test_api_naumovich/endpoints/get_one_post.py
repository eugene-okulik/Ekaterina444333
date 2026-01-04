import allure
import requests

from test_api_naumovich.endpoints.endpoint import Endpoint


class GetOneObject(Endpoint):
    @allure.step('Get one object')
    def one_object(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        return self.response
