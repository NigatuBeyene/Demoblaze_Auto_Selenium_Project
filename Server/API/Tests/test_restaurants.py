import allure
import requests
from Server.API.Constants.restaurants_constants import RestaurantsConstants

class Test_Restaurants:

    @allure.description('Get single restaurant with correctly data')
    def test_get_single_restaurant_correctly(self):
        value_id = RestaurantsConstants.value_id
        value_name = RestaurantsConstants.value_name
        url = RestaurantsConstants.url_restaurants
        res = requests.get(url+value_id)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 15
        assert res_data[RestaurantsConstants.success_key] == True
        assert res_data[RestaurantsConstants.restaurant_key][RestaurantsConstants.name_key] == value_name

    @allure.description('Get single restaurant with incorrectly data')
    def test_get_restaurant_data_incorrectly(self):
        value_id = RestaurantsConstants.value_id_illegal
        url = RestaurantsConstants.url_restaurants
        res = requests.get(url+value_id)
        res_data = res.json()
        assert res.status_code == 500
        assert res_data[RestaurantsConstants.success_key] == False
        assert res_data[RestaurantsConstants.message_key] == f'Cast to ObjectId failed for value "{value_id}" ' \
                                      '(type string) at path "_id" for model "Restaurant"'

    @allure.description('Get all the data from restaurants')
    def test_get_all_the_restaurants(self):
        res = requests.get(RestaurantsConstants.url_restaurants)
        res_data = res.json()
        number_of_records = len(res_data[RestaurantsConstants.data_key])
        assert res.status_code == 200
        assert res_data[RestaurantsConstants.success_key] == True
        assert number_of_records == 65



