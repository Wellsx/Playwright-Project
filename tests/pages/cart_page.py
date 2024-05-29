from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_product_title = self.page.locator('span.a-truncate-cut')
        self.cart_button = page.locator("#nav-cart")
        self.cart_quantity = page.locator("#quantity")
        
    def open_cart(self) -> None:
        self.cart_button.click()
        
    def add_quantity(self, qty) -> None:
        self.cart_quantity.select_option(qty)
        
        