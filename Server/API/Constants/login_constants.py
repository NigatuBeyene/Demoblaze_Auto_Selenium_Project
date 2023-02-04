
class Login_Id:

    URL = "https://api.demoblaze.com/login"
    LOGIN_BUTTON = "//a[@id='login2']" ## XPATH
    NAME = "loginusername"
    PASSWORD = "loginpassword"
    LOGIN_CLICK = "//button[contains(text(),'Log in')]"
    data_valid = {"username":"nigatu","password":"MzIxNA=="}
    data_invalid_user = {"username":"wertyu","password":"MzIxNA=="}
    data_invalid_password = {"username":"nigatu","password":"NA=="}