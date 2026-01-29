from pages.products_page import ProductsPage

class TestProducts:
    def test_add_and_remove(self, logged_driver):        
        products_page = ProductsPage(logged_driver)

        products_page.add_product(0)  
        products_page.add_product(1)  
        products_page.add_product(2)  
        
        assert products_page.get_cart_badge_count() == 3
        
        products_page.remove_product(1)

        assert products_page.get_cart_badge_count() == 2
        
        assert "inventory.html" in logged_driver.current_url
