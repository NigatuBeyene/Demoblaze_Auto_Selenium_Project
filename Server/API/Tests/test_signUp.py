from Server.API.Constants import signUp_constants
from Server.API.Constants.signUp_constants import SignUp_Id
import allure
import requests


class Test_Login:
    @allure.description('Login correctly')
    def test_signUp_correctly(self):
        url = SignUp_Id.URL
        data = SignUp_Id.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

        # assert res_data[signUp_constants.success_key] == False
        # assert res_data[signUp_constants.message_key] == "user with that email already exists"

    @allure.description('Login when password incorrectly')
    def test_signUp_with_incorrectly_password(self):
        url = SignUp_Id.URL
        data = SignUp_Id.data_invalid_password
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description('Login when user name incorrectly')
    def test_signUp_with_incorrectly_userName(self):
        url = SignUp_Id.URL
        data = SignUp_Id.data_invalid_user
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description('Login when user name & password incorrectly')
    def test_signUp_with_incorrectly_userName_and_password(self):
        url = SignUp_Id.URL
        data = SignUp_Id.data_invalid_user
        data1 = SignUp_Id.data_invalid_password
        res = requests.post(url, json=data)
        res1 = requests.post(url, json=data1)
        res_data = res.json()
        res_data1 = res1.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res1.status_code == 200
        assert res1.elapsed.total_seconds() < 10
