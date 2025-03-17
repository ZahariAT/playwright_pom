from playwright.sync_api import Page


class ShoppingCartPage:
    def __init__(self, page: Page):
        self.page = page
        self.update_shopping_list_locator = page.get_by_role('button', name='Update shopping cart')

    def verify_shopping_cart_items(self, expected_items: list[str]):
        for item in expected_items:
            assert self.page.locator(f'//a[text()="{item}" and @class="product-name"]').is_visible(
                timeout=30000), f'Item {item} not found!'

    def remove_item(self, product_name: str):
        self.page.locator(f'//a[contains(text(), "{product_name}")]/ancestor::tr//input[@type="checkbox"]').check()
        self.update_shopping_list_locator.click()

    def clear_shopping_cart(self):
        pass

    def is_shopping_cart_empty(self):
        pass
