from pages.checkout_page import CheckoutPage

class TestCheckout:
    
    def test_checkout(self, cart_with_products, data_checkout):
        
        checkout_page = CheckoutPage(cart_with_products)
        
        checkout_page.navigate_shopping_cart_link()
        
        assert "cart.html" in cart_with_products.current_url
        assert checkout_page.get_cart_badge_count() == 2
        
        checkout_page.remove_product(0)
        assert checkout_page.get_cart_badge_count() == 1
        
        checkout_page.click_checkout()
        
        checkout_page.fill_first_name(data_checkout["first_name"])
        checkout_page.fill_last_name(data_checkout["last_name"])
        checkout_page.fill_postal_code(data_checkout["postal_code"])
        
        checkout_page.click_continue()

        checkout_page.click_finish()
        assert "checkout-complete.html" in cart_with_products.current_url

        checkout_page.click_back_to_products()
        assert "inventory.html" in cart_with_products.current_url
