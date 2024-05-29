# tests/conftest.py
import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from tests.pages.home_page import HomePage
from tests.pages.search_result_page import SearchResultPage
from tests.pages.cart_page import CartPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def browser_context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    page.set_default_timeout(10000)
    yield page
    page.close()

@pytest.fixture(scope="function")
def home_page(page: Page) -> HomePage:
    home_page = HomePage(page)
    home_page.visit()
    return home_page

@pytest.fixture(scope="function")
def search_result_page(home_page: HomePage) -> SearchResultPage:
    return home_page.search_product()

@pytest.fixture(scope="function")
def add_product_to_cart(search_result_page):
    search_result_page.add_to_cart()
    

@pytest.fixture(scope="function")
def cart_page(page: Page) -> CartPage:
    cart_page = CartPage(page)
    cart_page.open_cart()
    return cart_page