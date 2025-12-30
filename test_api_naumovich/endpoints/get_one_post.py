import allure
import requests

from test_api_naumovich.endpoints.endpoint import Endpoint


class GetOnePost(Endpoint):
    @allure.step('Get one post')
    def one_post(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        return self.response
