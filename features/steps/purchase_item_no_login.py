from selenium.webdriver.common.by import By
from behave import *
import time

USERNAME = 'nate123'
PASSWORD = '12345'


@when('User clicks shop now')
def step_impl(context):
    enter_shop = context.driver.find_element(By.LINK_TEXT, "Shop Now")
    enter_shop.click()
    context.driver.save_screenshot("./purchase/enter_shop.png")
    time.sleep(0.25)


@when('User clicks on watch')
def step_impl(context):
    url = "/shop/7"
    watch_item = context.driver.find_element(By.XPATH, '//a[@href="' + url + '"]')
    watch_item.click()
    context.driver.save_screenshot("./purchase/watch.png")
    time.sleep(0.25)


@when('User clicks add to cart')
def step_impl(context):
    add_to_cart = context.driver.find_element(By.ID, "add-to-cart-button")
    add_to_cart.click()
    # If user is not logged in, the uri will either be cart or auth/login if it did not get redirected.
    # If user is logged in then the uri will be cart. If the uri is anything else It's because the quantity
    # has been exceeded.
    assert (context.driver.current_url == 'http://localhost:5000/cart'
            or context.driver.current_url == 'http://localhost:5000/auth/login')
    context.driver.save_screenshot("./purchase/add-to-cart-failed.png")
    time.sleep(0.25)
