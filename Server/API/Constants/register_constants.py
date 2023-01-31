from Server.API.Constants.login_constants import LoginConstants
from random import randint

class RegisterConstants(LoginConstants):
    num = randint(1, 2500)
    url_register = 'https://trip-yoetz.herokuapp.com/auth/register'
    data_valid = {'birthDate': "2000-02-02",
                  'email': f"yoss{num}@ss.com",
                  'lastName': "Meshuulam",
                  'name': "Avi",
                  'password': "123456"}
    data_invalid = {'birthDate': "2000-02-02",
                    'email': "yossi111@ss.com",
                    'lastName': "Meshuulam",
                    'name': "Avi",
                    'password': "123456"}