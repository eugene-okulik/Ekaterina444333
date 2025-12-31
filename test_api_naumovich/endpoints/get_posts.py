import allure
import requests

from test_api_naumovich.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step('Get a objects')
    def all_objects(self):
        self.response = requests.get(f'{self.url}')
        return self.response
