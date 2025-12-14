import requests


def object_for_id():
    body = {
        "name": "Kate",
        "data": {"city": "Petrozavodsk", "age": 24}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    object_id = response.json()['id']
    return object_id


def clear(object_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


def all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, 'Status code is incorrect'


def one_object(object_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'


def create_object():
    body = {
        "name": "Kate",
        "data": {"city": "Petrozavodsk", "age": 24}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json().get('name'), 'Name is required field'
    assert response.json().get('data'), 'Data is required field'


def put_object():
    object_id = object_for_id()
    body = {
        "name": "Katya",
        "data": {"city": "Moscow", "age": 23}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    ).json()
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json().get('name'), 'Name is required field'
    assert response.json().get('data'), 'Data is required field'
    clear(object_id)


def patch_object():
    object_id = object_for_id()
    body = {
        "name": "Katherine",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    ).json()
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json().get('name') or response.json().get('data'), 'You must fill in one of the fields'
    clear(object_id)


def delete_object():
    object_id = object_for_id()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'


delete_object()
