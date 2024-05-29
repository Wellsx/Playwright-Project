from playwright.sync_api import Page



class SearchResultPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_result_product = page.locator('//div[@data-index="4" and @data-component-type="s-search-result"]')
        self.search_result_product_title = self.search_result_product.locator('[data-cy="title-recipe"] span')
        self.search_result_product_add_to_cart_button = self.search_result_product.get_by_text("Add to Cart")
        
    def add_to_cart(self) -> None:
        self.search_result_product_add_to_cart_button.click(delay=1000)
        self.page.wait_for_selector("#nav-cart-count >> text=1")
