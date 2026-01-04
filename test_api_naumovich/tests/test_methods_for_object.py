import pytest

TEST_DATA = [
    {"name": "Julia", "data": {"city": "Spb", "age": 25}},
    {"name": "Daria", "data": {"city": "Msk", "age": 30}},
]


@pytest.mark.parametrize("data", TEST_DATA)
def test_create_new_objects(create_object_endpoint, data):
    create_object_endpoint.create_new_object(body=data)
    create_object_endpoint.check_field_data_is_not_empty()
    create_object_endpoint.check_field_name_is_not_empty()
    create_object_endpoint.check_that_status_is_200()


def test_get_all_objects(get_object_endpoint):
    get_object_endpoint.all_objects()
    get_object_endpoint.check_that_status_is_200()


def test_get_one_object(get_one_object_endpoint, object_id):
    get_one_object_endpoint.one_object(object_id)
    get_one_object_endpoint.check_that_status_is_200()


def test_put_object(update_object_endpoint, object_id):
    body = {
        "name": "Katya",
        "data": {"city": "Moscow", "age": 23},
    }
    update_object_endpoint.make_changes_in_object(object_id, body)
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_field_data_is_not_empty()
    update_object_endpoint.check_field_name_is_not_empty()


def test_patch_object(change_object_endpoint, object_id):
    body = {
        "name": "Katherine",
        "data": {},
    }
    change_object_endpoint.make_patch_changes_in_object(object_id, body)
    change_object_endpoint.check_that_status_is_200()
    change_object_endpoint.check_fields_name_or_data_is_not_empty()


def test_delete_object(delete_one_object_endpoint, object_id):
    delete_one_object_endpoint.delete_object(object_id)
    delete_one_object_endpoint.check_that_status_is_200()
