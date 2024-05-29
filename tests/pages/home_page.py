from playwright.sync_api import Page
from test_config.config import testConfig
from tests.pages.search_result_page import SearchResultPage
from tests.pages.cart_page import CartPage



class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_bar = page.locator("#twotabsearchtextbox")
        self.search_button = page.locator("#nav-search-submit-button")
        self.cart_button = page.locator("#nav-cart")
       
    def visit(self) -> None:
        self.page.goto(testConfig.baseUrl)
        
    def search_product(self) -> SearchResultPage:
        self.search_bar.fill(testConfig.test_product)
        self.search_button.click()
        return SearchResultPage(self.page)
    
    def open_cart(self) -> CartPage:
        self.cart_button.click()
        return CartPage(self.page)