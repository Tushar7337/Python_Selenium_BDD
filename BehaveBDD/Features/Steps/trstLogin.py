from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Launch the web URL and navigate to Login screen')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://qa.trsthealth.com/login")


@when(u'Enter username as "{useename}" and password as "{password}"')
def step_impl(context,useename,password):
    print(useename,'\n', password)
    username_input = context.driver.find_element(By.XPATH,"//input[@name='user']")
    username_input.send_keys(useename)

    pass_input = context.driver.find_element(By.XPATH,"//input[@name='password']")
    pass_input.send_keys(password)


@when(u'Click Sign In Button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//*[text()='Sign In']").click()
    print("Test Case Passed")


@then(u'Dashboard should display')
def step_impl(context):
    expected_txt = 'User'
    assert (context.driver.find_element(By.XPATH,"//*[text()='User']")
            .text.__eq__(expected_txt))

    context.driver.quit()

