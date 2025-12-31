import pytest

from test_api_naumovich.endpoints.create_post import CreateNewObject
from test_api_naumovich.endpoints.update_post import UpdateObject
from test_api_naumovich.endpoints.change_post import ChangeObject
from test_api_naumovich.endpoints.delete_post import DeleteObject
from test_api_naumovich.endpoints.get_one_post import GetOneObject
from test_api_naumovich.endpoints.get_posts import GetObject


@pytest.fixture()
def create_object_endpoint():
    return CreateNewObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def get_one_object_endpoint():
    return GetOneObject()


@pytest.fixture()
def change_object_endpoint():
    return ChangeObject()


@pytest.fixture()
def delete_one_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id(create_object_endpoint, delete_one_object_endpoint):
    body = {
        "name": "Katya",
        "data": {"city": "Moscow", "age": 23},
    }
    create_object_endpoint.create_new_object(body)
    yield create_object_endpoint.object_id
    delete_one_object_endpoint.delete_object(object_id)
