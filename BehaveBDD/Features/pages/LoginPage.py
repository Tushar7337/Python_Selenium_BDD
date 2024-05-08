from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    email_address_field_xpath = "//input[@id='input-email']"
    password_field_xpath = "//input[@id='input-password']"
    login_buttin_xpath = "//input[@value='Login']"
    warning_message = "//*[text()='Warning: No match for E-Mail Address and/or Password.']"

    def enter_email_address(self,email_text):
        self.driver.find_element(By.XPATH,self.email_address_field_xpath).send_keys(email_text)

    def enter_password(self,password_text):
        self.driver.find_element(By.XPATH,self.password_field_xpath).send_keys(password_text)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_buttin_xpath).click()

    def verify_warning_message(self,expt_txt):
        return (self.driver.find_element(By.XPATH,self.warning_message)
         .text.__contains__(expt_txt))

