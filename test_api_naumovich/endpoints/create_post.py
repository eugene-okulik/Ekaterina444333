from test_api_naumovich.endpoints.endpoint import Endpoint
import requests
import allure

class CreateNewPost(Endpoint):
    object_id = None

    @allure.step('Create a post')
    def create_new_post(self, body, headers=None):
            headers = headers if headers else self.headers
            self.response = requests.post(
                self.url,
                json=body,
                headers=headers
            )
            self.json = self.response.json()
            self.object_id = self.json['id']
            return self.response