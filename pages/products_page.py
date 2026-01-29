from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.SITE_MAP = {
            "buttons":{
                "add_to_cart":{
                    "css":"btn_primary"
                }
            }
        }

    def add_product(self, index):
        buttons = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_primary")))
        buttons[index].click()