from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://demowebshop.tricentis.com/'

    def open(self):
        self.page.goto(self.url)

    def select_product(self, product_name: str):
        from playwright_pom.pages.product_page import ProductPage

        self.page.get_by_role('link', name=product_name, exact=True).click()
        return ProductPage(self.page)
