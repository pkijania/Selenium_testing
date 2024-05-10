from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os

class TestPage:
    def setup_class(self):
        web_driver_path = os.getenv("PATH_TO_DRIVE")
        if web_driver_path is None:
            raise Exception(f"WEB_DRIVER_PATH env variable is not set. Please define it, so it points to your edge web driver")
        self.driver = webdriver.Edge(web_driver_path)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()