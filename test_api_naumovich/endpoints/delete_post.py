import allure
import requests

from test_api_naumovich.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    @allure.step('Delete a object')
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        return self.response
