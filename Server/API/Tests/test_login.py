from Server.API.Constants.login_constants import LoginConstants
import allure
import requests

class Test_Login:
    @allure.description('Login correctly')
    def test_login_correctly(self):
        url = LoginConstants.url_login
        data = LoginConstants.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data[LoginConstants.success_key] == True
        assert res_data[LoginConstants.message_key] == 'login successful'

    @allure.description('Login when password incorrectly')
    def test_login_with_incorrectly_password(self):
        url = LoginConstants.url_login
        data = LoginConstants.data_invalid_password
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data[LoginConstants.success_key] == False
        assert res_data[LoginConstants.message_key] == "password or email incorrect"

    @allure.description('Login when email incorrectly')
    def test_login_with_incorrectly_email(self):
        url = LoginConstants.url_login
        data = LoginConstants.data_invalid_email
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data[LoginConstants.success_key] == False
        assert res_data[LoginConstants.message_key] == "no user found"

    @allure.description('Login when email & password incorrectly')
    def test_login_with_incorrectly_email_and_password(self):
        url = LoginConstants.url_login
        data = LoginConstants.data_invalid_password_and_email
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data[LoginConstants.success_key] == False
        assert res_data[LoginConstants.message_key] == "no user found"

    @allure.description('Login when email & password are null')
    def test_login_with_null_email_and_password(self):
        url = LoginConstants.url_login
        data = {}
        res = requests.post(url, data=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
        assert res_data[LoginConstants.success_key] == False
        assert res_data[LoginConstants.message_key] == 'no user found'




