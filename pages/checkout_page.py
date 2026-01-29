from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):       
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        self.SITE_MAP = {
            "fields":{
                "first_name":{
                    "id":"first-name"
                },
                "last_name":{
                    "id":"last-name"
                },
                "postal_code":{
                    "id":"postal-code"
                }
            },
            "buttons":{
                "shopping_cart_link":{
                    "css":".shopping_cart_link"
                },
                "checkout":{
                    "id":"checkout"
                },
                "continue":{
                    "id":"continue"
                },
                "finish":{
                    "id":"finish"
                },
                "back_to_products":{
                    "id":"back-to-products"
                }
            }
        }

    def navigate_shopping_cart_link(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.SITE_MAP["buttons"]["shopping_cart_link"]["css"])))
        button.click()

    def click_checkout(self):
        button = self.wait.until(EC.element_to_be_clickable((By.ID, self.SITE_MAP["buttons"]["checkout"]["id"])))
        button.click()

    def fill_first_name(self, first_name):
        textbox = self.wait.until(EC.presence_of_element_located((By.ID, self.SITE_MAP["fields"]["first_name"]["id"])))
        textbox.clear()
        textbox.send_keys(first_name)

    def fill_last_name(self, last_name):
        textbox = self.wait.until(EC.presence_of_element_located((By.ID, self.SITE_MAP["fields"]["last_name"]["id"])))
        textbox.clear()
        textbox.send_keys(last_name)

    def fill_postal_code(self, postal_code):
        textbox = self.wait.until(EC.presence_of_element_located((By.ID, self.SITE_MAP["fields"]["postal_code"]["id"])) )
        textbox.clear()
        textbox.send_keys(postal_code)

    def click_continue(self):
        button = self.wait.until(EC.element_to_be_clickable((By.ID, self.SITE_MAP["buttons"]["continue"]["id"])))
        button.click()

    def click_finish(self):
        button = self.wait.until(EC.element_to_be_clickable((By.ID, self.SITE_MAP["buttons"]["finish"]["id"])))
        button.click()

    def click_back_to_products(self):
        button = self.wait.until(EC.element_to_be_clickable((By.ID, self.SITE_MAP["buttons"]["back_to_products"]["id"])))
        button.click()

    
    
    
    