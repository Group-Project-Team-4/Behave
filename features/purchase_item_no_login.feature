Feature: Try purchasing an item without being logged in

  Scenario: Purchase an item not logged in
     Given User is on the shop page
      When User clicks shop now
      When User clicks on watch
      When User clicks add to cart
      Then the test should pass
