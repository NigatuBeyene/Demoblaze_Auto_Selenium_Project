from locust import HttpUser, constant, task
from Server.API.Constants.serach_constants import SearchConstants


class SearchTest_Loads(HttpUser):
    host = SearchConstants.url_search
    wait_time = constant(1)

    @task
    def get_all_cities(self):
        res = self.client.get('')
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @task
    def get_error_city_name_not_exist(self):
        res = self.client.get(SearchConstants.value_invalid)
        assert res.status_code == 404
        assert res.elapsed.total_seconds() < 10