# Selenium_testing
Repository consists of automatic tests for simple website "Saucedemo" written in selenium for python.
Tests are written according to Behavior Driven Development methodology and Page Object Model pattern.
Additionaly Allure Behave was implemented in order to create reports from tests

## Task
Buy "Sauce Labs Backpack" and "Sauce Labs Bike Light" from a "Swag Labs" page

### Commands to run the tests
- Run the test:
```
python -m behave
```
- Process the test results and save an HTML report into the allure-report directory:
```
allure generate
```
- View the report:
```
allure open
```
- Puts the test results into a temporary directory and then automatically open the main page of the report in a web browser:
```
allure serve
```
