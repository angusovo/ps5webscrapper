
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver.v2 as uc
import time
  
ADD_TO_CART ='//button[@class="button_E6SE9 primary_1oCqK addToCartButton_1op0t addToCartButton regular_1jnnf"]'
GO_TO_CART='//a[@class="button_E6SE9 primary_1oCqK goToCartButton_Co1Sx regular_1jnnf"]'
CONTINUE_TO_CHECKOUT ='//a[@class="button_E6SE9 primary_1oCqK continueToCheckout_3Dgpe regular_1jnnf"]'
GUEST_CHECKOUT ='//a[@class="_3Po4I guest-continue-link"]'
CONTINUE_TO_PAYMENT ='//button[@class="button_2MMWS primary_5qmKv continue-to-payment regular_XiOzA"]'
FINAL_CHECKOUT = '//button[@class="button_2MMWS primary_5qmKv continue-to-review regular_XiOzA"]'

EMAIL ="testing1234@gmail.com"
FIRSTNAME= "CHRIS"
LASTNAME = "BROWN"
PHONE ="4132341234"
ADDRESS ="1203, 321 Yonge St"
CITY = "Toronto"
PROVINCE = "ON"
POSTALCODE = "M1S0J1"
CARDNO = "0000000000000000"
EXP_MON = "1"
EXP_YEAR = "2026"
CVV = "234"

class WebDriver():
    def __init__(self, path):
        self.path = path
        
    def openDriver(self):
        self.driver = uc.Chrome()
        self.driver.get(self.path)
        time.sleep(3)
        self.order()
        self.driver.quit()

    def order(self):


        # Add to Cart
        self.onClick(ADD_TO_CART,"xpath")
        # Go to Cart
        self.onClick(GO_TO_CART,"xpath")
        # Continue to Checkout
        self.onClick(CONTINUE_TO_CHECKOUT,"xpath")
        # Assume we dont have member and continue with guest
        self.onClick(GUEST_CHECKOUT,"xpath")
        
        self.inputData('email',EMAIL)
        self.inputData('firstName',FIRSTNAME)
        self.inputData('lastName',LASTNAME)
        self.inputData('phoneNumber',PHONE)
        self.inputData('addressLine1',ADDRESS)
        self.inputData('city',CITY)
        self.inputData('regionCode',PROVINCE)
        self.inputData('postalCode',POSTALCODE)

        # Continue to payment
        self.onClick(CONTINUE_TO_PAYMENT,"xpath")

        self.inputData('shownCardNumber',CARDNO)
        self.inputData('expirationMonth', EXP_MON)
        self.inputData('expirationYear', EXP_YEAR)
        self.inputData('cvv', CVV)

        # # Continue to check out
        self.onClick(FINAL_CHECKOUT,"xpath")

        # If the payment is success, you will receive a confirmation email 

    def onClick(self,path, type):
        try:
            print(f"try {path} with {type}")

            if type == "class":
                self.driver.find_element(By.CLASS_NAME,path).click()
            elif type == "id":
                self.driver.find_element(By.ID,path).click()
            elif type == "name":
                self.driver.find_element(By.NAME,path).click()
            elif type == "xpath":
                self.driver.find_element(By.XPATH,path).click()
            pass
        except Exception:
            time.sleep(1)
            self.onClick(path, type)

    def inputData(self,path,data):
        try:
            print(f"try {path} with {data}")
            self.driver.find_element(By.ID,path).send_keys(data)
        except Exception:
            time.sleep(1)
            self.inputData(path,data)



