from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  

class BasePage:
    SITE_LINK = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.COMMON_ELEMENTS = {
            "buttons": {
                "remove_product": {
                    "class": "btn_secondary"
                }
            },
            "view":{
                "shopping_cart_badge":{
                    "class": "shopping_cart_badge"
                }
            }
        }
    
    def remove_product(self, index):
        buttons = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_secondary")))
        buttons[index].click()

    def get_cart_badge_count(self):
        try:
            badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            return int(badge.text)
        except:
            return 0

    