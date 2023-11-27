from selenium.webdriver.common.by import By
from behave import *
import time

USERNAME = 'nate123'
PASSWORD = '12345'


@when('User clicks register')
def step_impl(context):
    register_link = context.driver.find_element(By.ID, "base_register_anchor")
    register_link.click()
    time.sleep(0.25)
    assert context.driver.current_url == 'http://localhost:5000/auth/register'
    context.driver.save_screenshot("./register/register_page.png")


@when('User enters register credentials')
def step_impl(context):
    username_input = context.driver.find_element(By.ID, "register_username_textinput")
    username_input.send_keys(USERNAME)
    time.sleep(0.25)
    assert username_input.get_attribute('value') == 'nate123'
    password_input = context.driver.find_element(By.ID, "register_password_textinput")
    password_input.send_keys(PASSWORD)
    time.sleep(0.25)
    assert password_input.get_attribute('value') == '12345'
    context.driver.save_screenshot("./register/register_credentials.png")


@when('User registers')
def step_impl(context):
    register_button = context.driver.find_element(By.ID, "register_submit_button")
    register_button.click()
    time.sleep(0.25)
    assert context.driver.current_url == 'http://localhost:5000/'
    context.driver.save_screenshot("./register/register_success.png")
