from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self,driver):
        self.driver = driver

    first_name_text_field_xpath = "//input[@id='input-firstname']"
    last_name_text_field_xpath = "//input[@id='input-lastname']"
    emai_text_field_xpath = "//input[@id='input-email']"
    mobile_number_text_field_xpath = "//input[@id='input-telephone']"
    enter_password_text_field_xpath = "//input[@id='input-password']"
    confirm_password_text_field_xpath = "//input[@id='input-confirm']"
    agree_btn_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"
    account_created_text_xpath = "//*[text()='Congratulations! Your new account has been successfully created!']"
    newsletter_subscribe_radio_byn_xpath = "//input[@name='newsletter'][@checked='checked']"
    duplicate_email_error_message_xpath = "//div[@id='account-register']/div[1]"
    policy_error_message_xpath = "//div[@id='account-register']/div[1]"
    first_name_error_message_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_error_message_xpath = "//input[@id='input-lastname']/following-sibling::div"
    empty_email_error_message_xpath = "//input[@id='input-email']/following-sibling::div"
    empty_phone_number_error_message_xpath = "//input[@id='input-telephone']/following-sibling::div"
    empty_password_error_message_xpath = "//input[@id='input-password']/following-sibling::div"


    def enter_first_name(self,first_name):
        self.driver.find_element(By.XPATH,self.first_name_text_field_xpath).send_keys(first_name)

    def enter_last_name(self,last_name):
        self.driver.find_element(By.XPATH,self.last_name_text_field_xpath).send_keys(last_name)

    def enter_emailId(self,random_email):
        self.driver.find_element(By.XPATH,self.emai_text_field_xpath).send_keys(random_email)

    def enter_mobile_number(self,num):
        self.driver.find_element(By.XPATH,self.mobile_number_text_field_xpath).send_keys(num)

    def enter_password(self,first_pass):
        self.driver.find_element(By.XPATH,self.enter_password_text_field_xpath).send_keys(first_pass)

    def enter_confirm_password(self,conf_pass):
        self.driver.find_element(By.XPATH,self.confirm_password_text_field_xpath).send_keys(conf_pass)

    def check_agree_btn(self):
        self.driver.find_element(By.XPATH,self.agree_btn_xpath).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH,self.continue_button_xpath).click()

    def verify_account_created_text(self,expt_txt):
        return (self.driver.find_element(By.XPATH,self.account_created_text_xpath)
         .text.__contains__(expt_txt))

    def click_newsletter_radio_btn(self):
        self.driver.find_element(By.XPATH,self.newsletter_subscribe_radio_byn_xpath).click()

    def verify_error_message_for_duplicate_email(self,error_msg):
        return (self.driver.find_element(By.XPATH,self.duplicate_email_error_message_xpath)
         .text.__contains__(error_msg))

    def verify_policy_error_message(self,policy_error):
        return (self.driver.find_element(By.XPATH,self.policy_error_message_xpath)
         .text.__contains__(policy_error))

    def verify_first_name_error_message(self,firstname_error):
        return (self.driver.find_element(By.XPATH,self.first_name_error_message_xpath)
         .text.__eq__(firstname_error))

    def verify_last_name_error_message(self,lastname_error):
        return (self.driver.find_element(By.XPATH,self.last_name_error_message_xpath)
         .text.__eq__(lastname_error))

    def verify_error_message_for_empty_email_text_field(self,email_error):
        return (self.driver.find_element(By.XPATH,self.empty_email_error_message_xpath)
         .text.__eq__(email_error))

    def verify_error_message_for_empty_phone_number(self,num_error):
        return (self.driver.find_element(By.XPATH,self.empty_phone_number_error_message_xpath)
         .text.__eq__(num_error))

    def verify_error_message_for_empty_password_text_field(self,pass_error):
        return (self.driver.find_element(By.XPATH,self.empty_password_error_message_xpath)
         .text.__eq__(pass_error))
