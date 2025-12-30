import pytest

TEST_DATA = [
    {"name": "Julia", "data": {"city": "Spb", "age": 25}},
     {"name": "Daria", "data": {"city": "Msk", "age": 30}}
]

@pytest.mark.parametrize('data', TEST_DATA)
def test_new_post_id(create_post_endpoint, data):
    create_post_endpoint.create_new_post(body=data)
    create_post_endpoint.check_field_data_is_not_empty()
    create_post_endpoint.check_field_name_is_not_empty()
    create_post_endpoint.check_that_status_is_200()

def test_get_all_objects(get_post_endpoint):
    get_post_endpoint.all_post()
    get_post_endpoint.check_that_status_is_200()

def test_get_one_object(get_one_post_endpoint, object_id):
    get_one_post_endpoint.one_post(object_id)
    get_one_post_endpoint.check_that_status_is_200()

def test_put_object(update_post_endpoint, object_id):
    body = {
        "name": "Katya",
        "data": {"city": "Moscow", "age": 23}
    }
    update_post_endpoint.make_changes_in_post(object_id, body)
    update_post_endpoint.check_that_status_is_200()
    update_post_endpoint.check_field_data_is_not_empty()
    update_post_endpoint.check_field_name_is_not_empty()

def test_patch_object(change_post_endpoint, object_id):
    body = {
        "name": "Katherine",
        "data": {}
    }
    change_post_endpoint.make_patch_changes_in_post(object_id, body)
    change_post_endpoint.check_that_status_is_200()
    change_post_endpoint.check_fields_name_or_data_is_not_empty()

def test_delete_object(delete_one_post_endpoint, object_id):
    delete_one_post_endpoint.delete_post(object_id)
    delete_one_post_endpoint.check_that_status_is_200()
