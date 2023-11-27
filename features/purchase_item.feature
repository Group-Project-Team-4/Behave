Feature: User purchases an item

  Scenario: Purchase an item
     Given User is on the shop page
      When User clicks login
      When User enters login credentials
      When User logs in
      When User clicks shop now
      When User clicks on watch
      When User clicks add to cart
      When User clicks checkout
      When User enters checkout info
      When User clicks pay
      Then the test should pass
