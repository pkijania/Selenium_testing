Feature: Basic operations
    Tests checking compliance of basic operations like logging in and out or adding products to the cart

Scenario: Logging in
    Given I am an unauthenticated user
    When I type "standard_user" username and "secret_sauce" password to the input fields and login
    Then I login successfully
"""
Scenario: Adding products to the basket
    Given I am an authenticated user
    When I add to cart "Sauce Labs Backpack" and "Sauce Labs Bike Light" items
        And I navigate to checkout
    Then The items are added to the basket

Scenario: Validating the purchase
    Given I am an authenticated user with some items in basket
        And I am on the checkout page
    When I provide my info: "John", "Smith", "54-254"
        And finish checkout
    Then Checkout is completed

Scenario: Logging out
    Given I am authenticated user
    When I logout
    Then I land on the logging page
"""