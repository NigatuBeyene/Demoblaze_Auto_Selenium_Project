import allure
import requests as requests

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


