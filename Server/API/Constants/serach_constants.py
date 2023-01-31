from Server.API.Constants.login_constants import LoginConstants

class SearchConstants(LoginConstants):
    url_search = "https://trip-yoetz.herokuapp.com/api/cities/"
    value_valid = 'Miami'
    value_invalid = 'Tel-Aviv'
    value_illegal = '1111'
    data_key = 'data'
    name_key = 'name'
