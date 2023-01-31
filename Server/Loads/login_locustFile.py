from Server.API.Constants.login_constants import LoginConstants
from locust import HttpUser, constant, task

class LoginTest_Loads(HttpUser):
    host = LoginConstants.url_login
    wait_time = constant(1)

    @task
    def user_login(self):
        res = self.client.post('', data=LoginConstants.data_valid)
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10


