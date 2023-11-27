from selenium import webdriver
from behave import *

@given('User is on the shop page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://localhost:5000/')
    assert context.driver.current_url == 'http://localhost:5000/'
    context.driver.save_screenshot("./login/main_page.png")

@then('the test should pass')
def step_impl(context):
    context.driver.quit()
    print("The test has passed")
