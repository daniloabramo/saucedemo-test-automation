from pages.login_page import LoginPage

class TestLogin:
    def valid_credentials(self, driver, valid_credentials):
        login_page = LoginPage(driver)
        
        login_page.navigate_to_login()
        
        login_page.login(
            valid_credentials["username"],
            valid_credentials["password"]
        )
    
        assert "inventory.html" in driver.current_url

    def invalid_credentials(self, driver, invalid_credentials):
        login_page = LoginPage(driver)
        
        login_page.navigate_to_login()
        login_page.login(
            invalid_credentials["username"],
            invalid_credentials["password"]
        )
        
        assert driver.current_url == "https://www.saucedemo.com/"

    def locked_user_credentials(self, driver, locked_user_credentials):
        login_page = LoginPage(driver)
        
        login_page.navigate_to_login()
        login_page.login(
            locked_user_credentials["username"],
            locked_user_credentials["password"]
        )
        
        assert driver.current_url == "https://www.saucedemo.com/"

    def problem_user_credentials(self, driver, problem_user_credentials):
        login_page = LoginPage(driver)
        
        login_page.navigate_to_login()
        login_page.login(
            problem_user_credentials["username"],
            problem_user_credentials["password"]
        )
        
        assert driver.current_url == "https://www.saucedemo.com/"


