from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        self.SITE_MAP = {
            "fields":{
                "username":{
                    "id":"user-name"
                },
                "password":{
                    "id":"password"
                }

            },
            "buttons":{
                "login":{
                    "id":"login-button"
                }
            }
        }

    def navigate_to_login(self):
        self.driver.get(self.SITE_LINK)

    def fill_username(self, username):
        textbox = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, self.SITE_MAP["fields"]["username"]["id"])
            )
        )
        textbox.clear()
        textbox.send_keys(username)

    def fill_password(self, password):
        textbox = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, self.SITE_MAP["fields"]["password"]["id"])
            )
        )
        textbox.clear()
        textbox.send_keys(password)

    def click_login_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, self.SITE_MAP["buttons"]["login"]["id"])
            )
        )
        button.click()

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()

    