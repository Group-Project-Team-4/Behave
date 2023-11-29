Feature: Logout functionality on the clothing store app

  Scenario: Logged in user can logout
    Given User is on the shop page
    When User clicks login
    When User enters login credentials
    When User logs in
    When User clicks logout
    Then the test should pass
