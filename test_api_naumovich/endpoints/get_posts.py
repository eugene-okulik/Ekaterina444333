import allure
import requests

from test_api_naumovich.endpoints.endpoint import Endpoint


class GetPost(Endpoint):
    @allure.step('Get a post')
    def all_post(self):
        self.response = requests.get(f'{self.url}')
        return self.response
