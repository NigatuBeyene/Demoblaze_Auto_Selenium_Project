import requests
import allure
from Server.API.Constants.register_constants import RegisterConstants

class Test_Register:
    @allure.description('User registered correctly')
    def test_user_register_correctly(self):
        url = RegisterConstants.url_register
        data = RegisterConstants.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data[RegisterConstants.success_key] == True
        assert res_data[RegisterConstants.message_key] == 'user added successfully'

    @allure.description('User registered with exist email')
    def test_user_register_incorrectly_with_exist_email(self):
        url = RegisterConstants.url_register
        data = RegisterConstants.data_invalid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data[RegisterConstants.success_key] == False
        assert res_data[RegisterConstants.message_key] == "user with that email already exists"

    def test_user_register_incorrectly_with_null_body(self):
        url = RegisterConstants.url_register
        data = {}
        res = requests.post(url, json=data)
        assert res.status_code == 400