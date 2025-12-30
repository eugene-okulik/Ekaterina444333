import pytest

from test_api_naumovich.endpoints.create_post import CreateNewPost
from test_api_naumovich.endpoints.update_post import UpdatePost
from test_api_naumovich.endpoints.change_post import ChangePost
from test_api_naumovich.endpoints.delete_post import DeletePost
from test_api_naumovich.endpoints.get_one_post import GetOnePost
from test_api_naumovich.endpoints.get_posts import GetPost


@pytest.fixture()
def create_post_endpoint():
    return CreateNewPost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def get_post_endpoint():
    return GetPost()


@pytest.fixture()
def get_one_post_endpoint():
    return GetOnePost()


@pytest.fixture()
def change_post_endpoint():
    return ChangePost()


@pytest.fixture()
def delete_one_post_endpoint():
    return DeletePost()


@pytest.fixture()
def object_id(create_post_endpoint):
    body = {
        "name": "Katya",
        "data": {"city": "Moscow", "age": 23},
    }
    create_post_endpoint.create_new_post(body)
    yield create_post_endpoint.object_id
