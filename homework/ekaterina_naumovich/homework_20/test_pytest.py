import pytest
import requests


@pytest.fixture
def object_for_id():
    body = {
        "name": "Kate",
        "data": {"city": "Petrozavodsk", "age": 24}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.fixture
def before_after():
    print('before test')
    yield
    print('after test')


@pytest.fixture(scope='session')
def start_end():
    print('Start testing')
    yield
    print('Testing completed')


def test_get_all_objects(before_after, start_end):
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, 'Status code is incorrect'


def test_get_one_object(before_after, object_for_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_for_id}')
    assert response.status_code == 200, 'Status code is incorrect'


@pytest.mark.parametrize('signup', [{"name": "Julia", "data": {"city": "Spb", "age": 25}},
                                    {"name": "Daria", "data": {"city": "Msk", "age": 30}}])
def test_create_new_object(signup, before_after):
    body = {
        "name": signup["name"],
        "data": signup["data"]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json().get('name'), 'Name is required field'
    assert response.json().get('data'), 'Data is required field'


@pytest.mark.critical
def test_put_object(before_after, object_for_id):
    body = {
        "name": "Katya",
        "data": {"city": "Moscow", "age": 23}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_for_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json().get('name'), 'Name is required field'
    assert response.json().get('data'), 'Data is required field'


@pytest.mark.medium
def test_patch_object(before_after, object_for_id):
    body = {
        "name": "Katherine",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_for_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json().get('name') or response.json().get('data'), 'You must fill in one of the fields'


def test_delete_object(before_after, object_for_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_for_id}')
    assert response.status_code == 200, 'Status code is incorrect'
