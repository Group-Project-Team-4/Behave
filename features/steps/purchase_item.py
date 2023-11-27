from selenium.webdriver.common.by import By
from behave import *
import time

@when('User clicks checkout')
def step_impl(context):
    checkout = context.driver.find_element(By.LINK_TEXT, "Checkout")
    checkout.click()
    context.driver.save_screenshot("./purchase/checkout.png")
    time.sleep(0.25)

@when('User enters checkout info')
def step_impl(context):
    email = context.driver.find_element(By.ID, "email")
    email.send_keys('nwschainblatt@my.waketech.edu')
    time.sleep(0.25)

    fullname = context.driver.find_element(By.ID, "name")
    fullname.send_keys('Nate Schainblatt')
    time.sleep(0.25)

    address = context.driver.find_element(By.ID, "address")
    address.send_keys('1234 abc st')
    time.sleep(0.25)

    card_number = context.driver.find_element(By.ID, "credit-card")
    card_number.send_keys('9234672322123467')
    time.sleep(0.25)

    expiration = context.driver.find_element(By.ID, "expiration-date")
    expiration.send_keys('03/27')
    time.sleep(0.25)

    card_pin = context.driver.find_element(By.ID, "cvc")
    card_pin.send_keys('473')
    context.driver.save_screenshot("./purchase/checkout_form_filled.png")


@when('User clicks pay')
def step_impl(context):
    purchase = context.driver.find_element(By.CLASS_NAME, "checkout-button")
    purchase.click()
    assert context.driver.current_url == 'http://localhost:5000/checkout/success'
    context.driver.save_screenshot("./purchase/items_purchased.png")
    time.sleep(0.25)
