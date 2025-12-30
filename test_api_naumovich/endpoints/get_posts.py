from test_api_naumovich.endpoints.endpoint import Endpoint
import requests
import allure

class GetPost(Endpoint):

    @allure.step('Get a post')
    def all_post(self):
        self.response = requests.get(f'{self.url}')
        return self.response