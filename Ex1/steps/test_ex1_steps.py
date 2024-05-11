from behave import *
from selenium.webdriver.common.by import By

@given("I am unauthenticated user")
def step_impl(context):
    pass

@when("I login with {standard_user:s} username and {secret_sauce:s} password")
def step_impl(context, user, password):
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()
"""
@then("I am succesfully logged in")
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Logout").visible().equals(True)

@given("I am an authenticated user")
def step_impl(context):
    pass

@when("I add to cart Sauce Labs Backpack and Sauce Labs Bike Light items")
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    context.driver.find_element(By.XPATH, "//span[text()='2']").click()
    context.driver.find_element(By.NAME, "checkout").click()

@given("I am an authenticated user with some items in basket")
def step_impl(context):
    pass

@when("I provide my info: John, Smith, 54-254")
def step_impl(context):
    context.driver.find_element(By.NAME, "firstName").send_keys("John")
    context.driver.find_element(By.NAME, "lastName").send_keys("Smith")
    context.driver.find_element(By.NAME, "postalCode").send_keys("54-254")
    context.driver.find_element(By.NAME, "continue").click()
    context.driver.find_element(By.NAME, "finish").click()
    context.driver.find_element(By.NAME, "back-to-products").click()

@given("I am authenticated user")
def step_impl(context):
    pass

@when("I logout")
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    context.driver.implicitly_wait(3)
    context.driver.find_element(By.LINK_TEXT, "Logout").click()
"""