import random

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

from Features.pages.AccountPage import AccountPage
from Features.pages.HomePage import HomePage
from Features.pages.LoginPage import LoginPage
from utilities import TimestampGenerator


@given(u'I Launch the Browser and Navigate to Login Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.select_login_option()

@when(u'I enter valid email as "{email}" and valid password as "{password}"')
def step_impl(context,email,password):
    print(email)
    print(password)
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I click Login Button')
def step_impl(context):
    context.login_page.click_on_login_button()


@then(u'I should get Logged In')
def step_impl(context):

    account_page = AccountPage(context.driver)
    assert account_page.status_of_account_information()


@when(u'I enter invalid email and valid password as "{password}"')
def step_impl(context,password):

    time = TimestampGenerator.enter_unique_email()
    print("----------------------",time)
    random_email = f'cuc{time}@gmail.com'

    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(random_email)

    context.login_page.enter_password(password)

@then(u'I should get proper warning message')
def step_impl(context):
    expt_txt = 'Warning: No match for E-Mail Address and/or Password.'
    assert context.login_page.verify_warning_message(expt_txt)


@when(u'I enter valid email as "{email}" and invalid as "{password}"')
def step_impl(context,email,password):
    try:
        print('----------------------------------------',email)
        print('----------------------------------------',password)
    except Exception as e:
        print(e)

    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I enter invalid email and invalid password')
def step_impl(context):

    wgn = TimestampGenerator.enter_unique_email()
    wrgn_email = f'cucu{wgn}@gmail.com'

    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(wrgn_email)

    generate = str(random.randint(100,900))
    context.login_page.enter_password(generate)



@when(u'I dont enter any email and password')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("")

    context.login_page.enter_password("")
