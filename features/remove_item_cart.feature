Feature: Removing item from cart functionality

  Scenario: User removes item from cart
    Given User is on the shop page
    When User clicks login
    When User enters login credentials
    When User logs in
    When User clicks shop now
    When User clicks on watch
    When User clicks add to cart
    Then User clicks remove
    Then the test should pass
