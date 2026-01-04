import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400

    @allure.step('Field name is not empty')
    def check_field_name_is_not_empty(self):
        assert self.json.get('name')

    @allure.step('Field data is not empty')
    def check_field_data_is_not_empty(self):
        assert self.json.get('data')

    @allure.step('Fields name or data is not empty')
    def check_fields_name_or_data_is_not_empty(self):
        assert (
            self.json().get('name') or self.json().get('data')
        ), 'You must fill in one of the fields'
