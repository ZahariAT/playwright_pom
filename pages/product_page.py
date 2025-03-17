from playwright.sync_api import Page
from playwright_pom.pages.shopping_cart_page import ShoppingCartPage


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_locator = page.locator('//input[contains(@id, "add-to-cart-button")]')
        self.shopping_cart_locator = page.locator('//span[contains(text(), "Shopping cart")]')
        self.home_page_locator = page.get_by_role('link', name='Home')

    def add_to_cart(self):
        self.add_to_cart_locator.click()

    def go_to_shopping_cart(self):
        self.shopping_cart_locator.click()
        return ShoppingCartPage(self.page)

    def return_to_home_page(self):
        from playwright_pom.pages.home_page import HomePage

        self.home_page_locator.click()
        return HomePage(self.page)
