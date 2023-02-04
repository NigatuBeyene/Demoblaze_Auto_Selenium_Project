class SignUp_Id:
    URL = "https://api.demoblaze.com/signup"

    SIGNUP_BUTTON = "//a[@id='signin2']"
    NAME = "sign-username"
    PASSWORD = "sign-password"
    SIGNIN_CLICK = " // button[contains(text(), 'Sign up')]"

    data_valid = {"username": "nigatu", "password": "MzIxNA=="}
    data_invalid_user = {"username": "wertyu", "password": "MzIxNA=="}
    data_invalid_password = {"username": "nigatu", "password": "NA=="}
    # success_key = {"SAFDSGH"}
    # message_key ={"werghjfyklg"}