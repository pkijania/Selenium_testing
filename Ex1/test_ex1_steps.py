from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

@given("I am on the logging in page of the website")
def step_impl(context):
    pass

@when("I type standard_user username and secret_sauce password to the input fields and press login button")
def step_impl(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()

@given("I am on the logging in page of the website")
def step_impl(context):
    pass

@when("I type standard_user username and secret_sauce password to the input fields and press login button")
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    context.driver.find_element(By.XPATH, "//span[text()='2']").click()
    context.driver.find_element(By.NAME, "checkout").click()

@given("I am on the logging in page of the website")
def step_impl(context):
    pass

@when("I type standard_user username and secret_sauce password to the input fields and press login button")
def step_impl(context):
    context.driver.find_element(By.NAME, "firstName").send_keys("John")
    context.driver.find_element(By.NAME, "lastName").send_keys("Smith")
    context.driver.find_element(By.NAME, "postalCode").send_keys("54-254")
    context.driver.find_element(By.NAME, "continue").click()
    context.driver.find_element(By.NAME, "finish").click()
    context.driver.find_element(By.NAME, "back-to-products").click()

@given("I am on the logging in page of the website")
def step_impl(context):
    pass

@when("I type standard_user username and secret_sauce password to the input fields and press login button")
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    context.driver.implicitly_wait(3)
    context.driver.find_element(By.LINK_TEXT, "Logout").click()
