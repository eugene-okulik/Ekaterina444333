from test_api_naumovich.endpoints.endpoint import Endpoint
import requests
import allure


class ChangePost(Endpoint):

    @allure.step('Change a post')
    def make_patch_changes_in_post(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json
        return self.response