from selenium.webdriver.common.by import By
from behave import *
import time

@then('User clicks remove')
def step_impl(context):
    remove_button = context.driver.find_element(By.CLASS_NAME, "cart-item-remove")
    remove_button.click()
    assert context.driver.current_url == 'http://localhost:5000/cart'
    context.driver.save_screenshot("./remove/empty_cart.png")
    time.sleep(0.25)