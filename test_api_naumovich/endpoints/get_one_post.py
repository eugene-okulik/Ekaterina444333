from test_api_naumovich.endpoints.endpoint import Endpoint
import requests
import allure

class GetOnePost(Endpoint):

    @allure.step('Get one post')
    def one_post(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        return self.response