from selenium.webdriver.common.by import By
from behave import *
import time

USERNAME = 'nate123'
PASSWORD = '12345'


@when('User clicks login')
def step_impl(context):
    login_link = context.driver.find_element(By.ID, "base_login_anchor")
    login_link.click()
    time.sleep(0.25)
    assert context.driver.current_url == 'http://localhost:5000/auth/login'
    context.driver.save_screenshot("./login/login_page.png")


@when('User enters login credentials')
def step_impl(context):
    username_input = context.driver.find_element(By.ID, "login_username_textinput")
    username_input.send_keys(USERNAME)
    time.sleep(0.25)
    assert username_input.get_attribute('value') == 'nate123'
    password_input = context.driver.find_element(By.ID, "login_password_textinput")
    password_input.send_keys(PASSWORD)
    time.sleep(0.25)
    assert password_input.get_attribute('value') == '12345'
    context.driver.save_screenshot("./login/login_credentials.png")


@when('User logs in')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, "login_submit_button")
    login_button.click()
    time.sleep(0.25)
    assert context.driver.current_url == 'http://localhost:5000/'
    context.driver.save_screenshot("./login/login_success.png")
