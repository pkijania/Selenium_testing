from selenium import webdriver
import os

def before_all(context):
    web_driver_path = os.getenv("PATH_TO_DRIVE")
    if web_driver_path is None:
        raise Exception(
            f"PATH_TO_DRIVE env variable is not set. Please define it, so it points to your edge web driver")
    driver = webdriver.Edge(web_driver_path)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    context.driver = driver
