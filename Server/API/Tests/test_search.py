from Server.API.Constants.serach_constants import SearchConstants
import requests
import allure

class Test_Search:
    @allure.description('Search correctly in the website')
    def test_search_correctly(self):
        value = SearchConstants.value_valid
        url = SearchConstants.url_search+value
        res = requests.get(url)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data[SearchConstants.success_key] == True
        assert res_data[SearchConstants.data_key][SearchConstants.name_key] == value

    @allure.description('Search incorrectly - city not exist')
    def test_search_incorrectly_when_city_not_exist(self):
        value = SearchConstants.value_invalid
        url = SearchConstants.url_search+value
        res = requests.get(url)
        res_data = res.json()
        assert res.status_code == 404
        assert res.elapsed.total_seconds() < 10
        assert res_data[SearchConstants.success_key] == False
        assert res_data[SearchConstants.message_key] == "no city found"

    @allure.description('Search incorrectly when city name invalid')
    def test_search_incorrectly_with_invalid_value(self):
        value = SearchConstants.value_illegal
        url = SearchConstants.url_search+value
        res = requests.get(url)
        res_data = res.json()
        assert res.status_code == 404
        assert res.elapsed.total_seconds() < 10
        assert res_data[SearchConstants.success_key] == False
        assert res_data[SearchConstants.message_key] == "no city found"
