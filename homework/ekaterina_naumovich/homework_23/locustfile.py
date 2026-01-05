from locust import task, HttpUser
import random


class Objects (HttpUser):

    @task(1)
    def get_all_objects(self):
        response = self.client.get('')

    @task(3)
    def get_one_object(self):
        id = {random.randint(25,30)}
        response = self.client.get(f'/{id}')
        assert(id == 29), 'Secret object'

    @task(2)
    def create_one_object(self):
        response = self.client.post(
            '',
            json={
                'name': 'Sam',
                'data': {
                    'city': 'Da Nang',
                    'age': '37'
                }
            }
        )
