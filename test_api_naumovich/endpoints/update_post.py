from test_api_naumovich.endpoints.endpoint import Endpoint
import requests
import allure

class UpdatePost(Endpoint):

    @allure.step('Update a post')
    def make_changes_in_post(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response