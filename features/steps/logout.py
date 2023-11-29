from selenium.webdriver.common.by import By
from behave import *
import time

@when('User clicks logout')
def step_impl(context):
    logout_button = context.driver.find_element(By.ID, "base_logout_anchor")
    logout_button.click()
    time.sleep(0.25)
    assert context.driver.current_url == 'http://localhost:5000/'
    context.driver.save_screenshot("./logout/main_page.png")