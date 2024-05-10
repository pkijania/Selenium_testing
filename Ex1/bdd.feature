Feature: Basic operations
    Tests checking compliance of basic operations like logging in and out or adding products to the cart

Scenario: Logging in
    Given I am on the "logging" in page of the website
    When I type "standard_user" username and "secret_sauce" password to the input fields and press "login" button
    Then I enter the main page of the website

Scenario: Adding products to the basket
    Given I am on the main page of the website
    When I click "Add to cart" button below "Sauce Labs Backpack" and "Sauce Labs Bike Light" items
        And I click the "basket" button and the "checkout" button
    Then The items are added to the basket
        And I proceed to the checkout page

Scenario: Validating the purchase
    Given I am on the checkout page
    When I type "John", "Smith", "54-254" to the correct input fields
        And I click the "continue", "finish" and "back home" buttons
    Then I enter the main page of the website

Scenario: Logging out
    Given I am on the checkout page
    When I click the "menu" button and the "logout" button
    Then I land on the logging in page of the website
