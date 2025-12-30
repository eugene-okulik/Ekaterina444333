from test_api_naumovich.endpoints.endpoint import Endpoint
import requests
import allure

class DeletePost(Endpoint):

    @allure.step('Delete a post')
    def delete_post(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        return self.response