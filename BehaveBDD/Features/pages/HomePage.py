from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    my_account_option_xpath = "//span[text()='My Account']"
    login_option = "Login"
    search_field_name = "search"
    search_btn_xpath = "//div[@id='search']//button"
    product_link_text = "HP LP3065"
    product_error_message_xpath = "//input[@id='button-search']/following-sibling::p"
    register_option_link_text = "Register"

    def click_on_my_account(self):
        self.driver.find_element(By.XPATH,self.my_account_option_xpath).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_option).click()

    def enter_value_in_search_field(self,product):
        self.driver.find_element(By.NAME,self.search_field_name).send_keys(product)

    def click_search_btn(self):
        self.driver.find_element(By.XPATH,self.search_btn_xpath).click()

    def verify_product(self):
        return self.driver.find_element(By.LINK_TEXT,self.product_link_text).is_displayed()

    def verify_product_error_message(self,expt_txt):
        return self.driver.find_element(By.XPATH,self.product_error_message_xpath).text.__eq__(expt_txt)

    def select_register_option(self):
        self.driver.find_element(By.LINK_TEXT,self.register_option_link_text).click()