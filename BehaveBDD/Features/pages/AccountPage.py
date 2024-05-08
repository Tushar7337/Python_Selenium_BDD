from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self,driver):
        self.driver =driver

    account_information_link_text = "Edit your account information"

    def status_of_account_information(self):
        return self.driver.find_element(By.LINK_TEXT,self.account_information_link_text).text.__eq__('Edit your account information')