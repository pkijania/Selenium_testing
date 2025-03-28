from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginLocators:
    user_name = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

class ProductsBasketLocators:
    add_to_cart_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_bike_light = (By.ID, "add-to-cart-sauce-labs-bike-light")
    button = (By.XPATH, "//span[text()='2']")
    checkout = (By.NAME, "checkout")
    information = (By.XPATH, "//span[text()='Checkout: Your Information']")

class PurchaseValidatorLocators:
    first_name = (By.NAME, "firstName")
    last_name = (By.NAME, "lastName")
    postal_code = (By.NAME, "postalCode")
    continue_button = (By.NAME, "continue")
    finish = (By.NAME, "finish")
    back_to_products = (By.NAME, "back-to-products")
    main_menu = (By.XPATH, "//span[text()='Products']")

class LogoutLocators:
    menu = (By.ID, "react-burger-menu-btn")
    logout = (By.LINK_TEXT, "Logout")
    exit_button = (By.ID, "react-burger-cross-btn")

class PositionValidator:
    @staticmethod
    def check_if_exists(driver, check):
        try:
            info = driver.find_element(*check).is_displayed()
            if info is True:
                return True
            else:
                return False
        except NoSuchElementException:
            return False

class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, standard_user, secret_sauce):
        self.driver.find_element(*LoginLocators.user_name).send_keys(standard_user)
        self.driver.find_element(*LoginLocators.password).send_keys(secret_sauce)
        self.driver.find_element(*LoginLocators.login_button).click()
    
    def login_exists(self):
        return PositionValidator.check_if_exists(self.driver, LoginLocators.login_button)

class ProductsBasket:
    def __init__(self, driver):
        self.driver = driver

    def add_products(self):
        self.driver.find_element(*ProductsBasketLocators.add_to_cart_backpack).click()
        self.driver.find_element(*ProductsBasketLocators.add_to_cart_bike_light).click()
        self.driver.find_element(*ProductsBasketLocators.button).click()
        self.driver.find_element(*ProductsBasketLocators.checkout).click()
    
    def info_exists(self):
        return PositionValidator.check_if_exists(self.driver, ProductsBasketLocators.information)
        
class PurchaseValidator:
    def __init__(self, driver):
        self.driver = driver

    def validate_purchase(self, name, surname, pcode):
        self.driver.find_element(*PurchaseValidatorLocators.first_name).send_keys(name)
        self.driver.find_element(*PurchaseValidatorLocators.last_name).send_keys(surname)
        self.driver.find_element(*PurchaseValidatorLocators.postal_code).send_keys(pcode)
        self.driver.find_element(*PurchaseValidatorLocators.continue_button).click()
        self.driver.find_element(*PurchaseValidatorLocators.finish).click()
        self.driver.find_element(*PurchaseValidatorLocators.back_to_products).click()
    
    def menu_exists(self):
        return PositionValidator.check_if_exists(self.driver, PurchaseValidatorLocators.main_menu)

class Logout:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(*LogoutLocators.menu).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*LogoutLocators.logout).click()

    def logout_exists(self):
        self.driver.find_element(*LogoutLocators.menu).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*LogoutLocators.exit_button).click()
        return PositionValidator.check_if_exists(self.driver, LogoutLocators.logout)
