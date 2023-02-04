class Place_Order:
    URL = "https://api.demoblaze.com/deletecart"
    CART = "//a[contains(text(),'Cart')]"
    REMOVE = "div.row div.col-lg-8 div.table-responsive:nth-child(2) table.table.table-bordered.table-hover.table-striped tbody:nth-child(2) tr.success td:nth-child(4) > a:nth-child(1)"
    PLACE_ORDER = "//button[contains(text(),'Place Order')]"
    NAME = "name"
    COUNTRY = "country"
    CITY = "city"
    CREDIT_CARD = "card"
    MONTH = "month"
    YEAR = "year"
    PURCHASE = "//button[contains(text(),'Purchase')]"
    CLOSE = "//body/div[@id='orderModal']/div[1]/div[1]/div[3]/button[1]"
    data_valid = {'cookie': "user=11f9573e-5d7b-1234-c075-a01aa1a9b98d"}
