Feature: Basic operations
    Tests checking compliance of basic operations like logging in and out or adding products to the cart

Scenario: Logging in
    Given I am an unauthenticated user
    When I type "standard_user" username and "secret_sauce" password to the input fields and login
    Then I login successfully

Scenario: Adding products to the basket
    Given I am an authenticated user
    When I add to cart "Sauce Labs Backpack" and "Sauce Labs Bike Light" items
    Then I land on checkout page

Scenario: Validating the purchase
    Given I am on checkout page
    When I provide my info: "John", "Smith", "54-254"
    Then Checkout is completed

Scenario: Logging out
    Given I am on main page
    When I logout
    Then I land on the logging page
