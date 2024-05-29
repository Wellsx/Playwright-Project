import pytest
from playwright.sync_api import Page, expect
from tests.pages.home_page import HomePage
from tests.pages.search_result_page import SearchResultPage
from tests.pages.cart_page import CartPage
from test_config.config import testConfig



def test_visit_home_page(home_page: HomePage) -> None:
    expect(home_page.search_bar).to_be_visible()
    expect(home_page.search_button).to_be_visible()
    
def test_search_product(search_result_page: SearchResultPage) -> None:
    expect(search_result_page.search_result_product).to_be_visible()
    expect(search_result_page.search_result_product_title).to_contain_text(testConfig.test_product)
    
def test_add_product_to_cart(add_product_to_cart, search_result_page, cart_page) -> None:
    expect(cart_page.cart_product_title).to_contain_text(testConfig.test_product)
      
def test_add_quantity(add_product_to_cart, cart_page) -> None:
    expect(cart_page.cart_quantity).to_be_visible()
    cart_page.add_quantity(testConfig.qty_amount)
    expect(cart_page.cart_quantity).to_have_value(testConfig.qty_amount)
    
    
    



    
    
    
    
     
    
    
    
