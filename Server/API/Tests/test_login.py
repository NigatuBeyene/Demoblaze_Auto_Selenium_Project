from Server.API.Constants.login_constants import Login_Id
import allure
import requests


class Test_Login:
    @allure.description('Login correctly')
    def test_login_correctly(self):
        url = Login_Id.URL
        data = Login_Id.data_valid
        res = requests.post(url, json=data)
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description('Login when password incorrectly')
    def test_login_with_incorrectly_password(self):
        url = Login_Id.URL
        data = Login_Id.data_invalid_password
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description('Login when user name incorrectly')
    def test_login_with_incorrectly_userName(self):
        url = Login_Id.URL
        data = Login_Id.data_invalid_user
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description('Login when user name & password incorrectly')
    def test_login_with_incorrectly_userName_and_password(self):
        url = Login_Id.URL
        data = Login_Id.data_invalid_user
        data1 = Login_Id.data_invalid_password
        res = requests.post(url, json=data)
        res1 = requests.post(url, json=data1)
        res_data = res.json()
        res_data1 = res1.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res1.status_code == 200
        assert res1.elapsed.total_seconds() < 10
