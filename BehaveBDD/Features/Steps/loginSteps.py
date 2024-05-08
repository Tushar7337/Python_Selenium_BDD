from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'Launch Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when(u'Open Login Screen')
def step_impl(context):
    context.driver.get("https://qa-emr.blueskytelepsychiatry.com/auth/login")

@when(u'Enter username "{username}" and password "{password}"')
def step_impl(context,username,password):
    print(username)
    print(password)
    wait = WebDriverWait(context.driver, 10)
    #context.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    #context.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    emailinput = wait.until(EC.presence_of_element_located(By.CSS_SELECTOR,"input[name='username']"))
    emailinput.send_keys(username)
    passwordinput = wait.until(EC.presence_of_element_located(By.CSS_SELECTOR,"input[name='password']"))
    passwordinput.send_keys(password)

@when(u'Click on Login Button')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[text()='Login']").click()

@then(u'Verify Dashboard of the application')
def step_impl(context):
    try:
        dash = context.driver.find_element_by_xpath("//*[text()='Dashboard']").text
    except:
        context.driver.close()
        assert False,"Test Failed"

    if dash == 'Dashboard':
    #assert dash == "Dashboard"
        assert True,'Test Passed'
        print(dash)
        context.driver.close()
