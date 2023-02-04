from Server.API.Constants.place_order_constants import Place_Order
import allure
import requests


class Test_Login:
    @allure.description('Login correctly')
    def test_place_order_correctly(self):
        url = Place_Order.URL
        data = Place_Order.data_valid
        res = requests.post(url, json=data)
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10