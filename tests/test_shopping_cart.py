import allure
import pytest
import uuid

from playwright_pom.pages.home_page import HomePage

PRODUCTS = [
    ('Build your own computer', '14.1-inch Laptop', 'Simple Computer'),
]


@pytest.mark.parametrize('product1, product2, product3', PRODUCTS)
def test_shopping_cart(page, product1, product2, product3):
    products_list = ['14.1-inch Laptop']
    product_1 = '14.1-inch Laptop'

    home_p = HomePage(page)

    try:
        # Step 1: Open homepage
        home_p.open()

        # Step 2: Add three products to the cart
        for prod in products_list:
            product_p = home_p.select_product(prod)
            product_p.add_to_cart()
            product_p.return_to_home_page()  # Go back to homepage

        # Step 3: Navigate to cart and verify items
        shopping_cart_p = product_p.go_to_shopping_cart()
        shopping_cart_p.verify_shopping_cart_items(products_list)

        # Step 4: Remove one product
        shopping_cart_p.remove_item(product_1)
        # shopping_cart_p.verify_shopping_cart_items([product2, product3])

        # Step 5: Clear the shopping_cart
        # shopping_cart_p.clear_shopping_cart()
        # assert shopping_cart_p.is_cart_empty(), "Cart is not empty after clearing!"

    except Exception as e:
        allure.attach(
            page.screenshot(),
            name=f'test_shopping_cart_{str(uuid.uuid4())[:4]}.png',
            attachment_type=allure.attachment_type.PNG,
        )
        raise e

    finally:
        page.close()
