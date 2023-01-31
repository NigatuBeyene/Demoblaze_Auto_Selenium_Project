

class LoginConstants:
    url_login = 'https://trip-yoetz.herokuapp.com/auth/login'
    success_key = 'success'
    message_key = 'message'
    data_valid = {"email": "Yosef@gmail.com", "password": "123456"}
    data_invalid_password = {"email": "Yosef@gmail.com", "password": "6116161616"}
    data_invalid_email = {"email": "m@fg", "password": "123456"}
    data_invalid_password_and_email = {"email": "m@fg", "password": "1223231184"}