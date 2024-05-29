Feature: Searching and adding item to cart

    As an online shopper, I want to search for a product on Amazon, add it to my basket, 
    and update the quantity of the item to ensure a seamless shopping experience.

    Scenario: Search for a product, add it to cart and update the item quantity.
        Given I am on the Amazon homepage.
        When I search for a product.
        And I click the "Add to cart" button on the first product in the search result page.
        Then I should see the product in my cart.
        When I click on the quantity drop down menu and select "2".
        Then The item quantity should increase to 2.