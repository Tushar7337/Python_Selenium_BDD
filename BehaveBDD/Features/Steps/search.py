from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from Features.pages.HomePage import HomePage


@given(u'I Launch the URL and navigated to Home Page')
def step_impl(context):
    print('Dashboard')
    try:
        context.home_page = HomePage(context.driver)
        assert context.home_page.check_home_page_title("Your Store")
    except Exception as e:
        print(e)

@when(u'I entered valid product say "{product}" in search box field')
def step_impl(context,product):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_value_in_search_field(product)

@when(u'I clicked on search Button')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_search_btn()

@then(u'Valid Product should get displayed in search result')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.verify_product()
    print('Test Passed')

@then(u'Proper message should be display in search result')
def step_impl(context):
    expt_txt = 'There is no product that matches the search criteria.'
    context.home_page = HomePage(context.driver)
    assert context.home_page.verify_product_error_message(expt_txt)


@when(u'I not entered anything in search box field')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_value_in_search_field("")

@when(u'I entered invalid product say "{product}" in search box field')
def step_impl(context,product):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_value_in_search_field(product)

