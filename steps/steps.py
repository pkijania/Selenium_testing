from selenium.webdriver.common.by import By
from automation import *
from behave import *

#1
@given("I am an unauthenticated user")
def step_impl(context):
    unauthenticated = Login(context.driver)
    assert unauthenticated.login_exists()

@when('I type "{user}" username and "{password}" password to the input fields and login')
def step_impl(context, user, password):
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()

@then('I login successfully')
def step_impl(context):
    login = Logout(context.driver)
    assert login.logout_exists()

#2
@given('I am an authenticated user')
def step_impl(context):
    authenticated = Logout(context.driver)
    assert authenticated.logout_exists()

@when('I add to cart "Sauce Labs Backpack" and "Sauce Labs Bike Light" items')
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    context.driver.find_element(By.XPATH, "//span[text()='2']").click()
    context.driver.find_element(By.NAME, "checkout").click()

@then('I land on checkout page')
def step_impl(context):
    info = ProductsBasket(context.driver)
    assert info.info_exists()

#3
@given("I am on checkout page")
def step_impl(context):
    checkout_start = ProductsBasket(context.driver)
    assert checkout_start.info_exists()

@when('I provide my info: "{name}", "{surname}", "{pcode}"')
def step_impl(context, name, surname, pcode):
    context.driver.find_element(By.NAME, "firstName").send_keys(name)
    context.driver.find_element(By.NAME, "lastName").send_keys(surname)
    context.driver.find_element(By.NAME, "postalCode").send_keys(pcode)
    context.driver.find_element(By.NAME, "continue").click()
    context.driver.find_element(By.NAME, "finish").click()
    context.driver.find_element(By.NAME, "back-to-products").click()

@then("Checkout is completed")
def step_impl(context):
    checkout_end = PurchaseValidator(context.driver)
    assert checkout_end.menu_exists()

#4
@given("I am on main page")
def step_impl(context):
    main_menu = PurchaseValidator(context.driver)
    assert main_menu.menu_exists()

@when("I logout")
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    context.driver.implicitly_wait(3)
    context.driver.find_element(By.LINK_TEXT, "Logout").click()

@then("I land on the logging page")
def step_impl(context):
    logout = Login(context.driver)
    assert logout.login_exists()
