import random

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from Features.pages.HomePage import HomePage
from Features.pages.RegisterPage import RegisterPage
from utilities import TimestampGenerator


@given(u'I launch the URL and navigate to Register Page')
def step_impl(context):

    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()

    context.home_page.select_register_option()

@when(u'I enter below details mandatory field')
def step_impl(context):
    for row in context.table:
        context.register_page = RegisterPage(context.driver)
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        print(row["first_name"])
        print(row["last_name"])

        num = TimestampGenerator.enter_unique_email()
        random_email = f'raw{num}@gmail.com'

        print(num)
        print(random_email)
        context.register_page.enter_emailId(random_email)
        context.register_page.enter_mobile_number(num)
        context.register_page.enter_password(row["password"])
        context.register_page.enter_confirm_password(row["password"])
        context.register_page.check_agree_btn()


@when(u'I click on Continue Button')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_continue_button()


@then(u'Account Should get created')
def step_impl(context):
    expt_txt = 'Congratulations'
    context.register_page = RegisterPage(context.driver)
    context.register_page.verify_account_created_text(expt_txt)

@when(u'I enter all the below field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])

        num = TimestampGenerator.enter_unique_email()
        random_email = f'raw{num}@gmail.com'
        print(num)
        print(random_email)
        context.register_page.enter_emailId(random_email)
        context.register_page.enter_mobile_number(num)
        context.register_page.enter_password(row["password"])
        context.register_page.enter_confirm_password(row["password"])
        context.register_page.click_newsletter_radio_btn()
        context.register_page.check_agree_btn()

@when(u'I enter existing email in email textfield')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])

        num = str(random.randint(1111111111, 9999999999))
        duplicate_email = 'raw@gmail.com'
        context.register_page.enter_emailId(duplicate_email)
        print(num)
        print('Existing Email',duplicate_email)
        context.register_page.enter_mobile_number(num)
        context.register_page.enter_password(row["password"])
        context.register_page.enter_confirm_password(row["password"])
        context.register_page.check_agree_btn()

@then(u'Proper error message about duplicate email should be display')
def step_impl(context):
    try:
        error_msg = 'Warning: E-Mail Address is already registered!'
        context.register_page = RegisterPage(context.driver)
        assert context.register_page.verify_error_message_for_duplicate_email(error_msg)
    except Exception as e:
        print(e)

@when(u'I dont enter any details')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_emailId("")
    context.register_page.enter_mobile_number("")
    context.register_page.enter_password("")
    context.register_page.enter_confirm_password("")


@then(u'Proper error message about mandatory fields should be display')
def step_impl(context):
    firstname_error = 'First Name must be between 1 and 32 characters!'
    lastname_error = 'Last Name must be between 1 and 32 characters!'
    email_error = 'E-Mail Address does not appear to be valid!'
    num_error = 'Telephone must be between 3 and 32 characters!'
    pass_error = 'Password must be between 4 and 20 characters!'
    policy_error = 'Warning: You must agree to the Privacy Policy!'

    context.register_page = RegisterPage(context.driver)

    context.register_page.verify_policy_error_message(policy_error)
    context.register_page.verify_first_name_error_message(firstname_error)
    context.register_page.verify_last_name_error_message(lastname_error)
    context.register_page.verify_error_message_for_empty_email_text_field(email_error)
    context.register_page.verify_error_message_for_empty_phone_number(num_error)
    context.register_page.verify_error_message_for_empty_password_text_field(pass_error)

