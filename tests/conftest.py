import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    
    chrome_options.add_experimental_option("prefs", prefs)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver  
    driver.quit() 


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

# Dados para Teste:
@pytest.fixture
def valid_credentials():
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }

@pytest.fixture
def invalid_credentials():
    return {
        "username": "invalid_user",
        "password": "wrong_password"
    }

@pytest.fixture
def locked_user_credentials():
    return {
        "username": "locked_out_user",
        "password": "secret_sauce"
    }

@pytest.fixture
def problem_user_credentials():
    return {
        "username": "problem_user",
        "password": "secret_sauce"
    }

@pytest.fixture(params=[
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce")
])
def multiple_valid_users(request):
    return {
        "username": request.param[0],
        "password": request.param[1]
    }

# Login:
@pytest.fixture
def logged_driver(driver, valid_credentials):
    """Fixture que retorna um driver já logado"""
    from pages.login_page import LoginPage
    
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_page.login(
        valid_credentials["username"],
        valid_credentials["password"]
    )
    
    return driver

# Checkout:
@pytest.fixture  
def cart_with_products(logged_driver):
    """Driver logado com produtos no carrinho"""
    from pages.products_page import ProductsPage
    
    products_page = ProductsPage(logged_driver)
    products_page.add_product(0)
    products_page.add_product(1)
    
    return logged_driver

@pytest.fixture
def data_checkout():
    """Retorna credenciais válidas para login"""
    return {
        "first_name": "João",
        "last_name": "Ferreiro",
        "postal_code": "01310000"
    }

# Alure:
import allure
import os
import inspect

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Erro ao capturar screenshot: {e}")


@pytest.fixture(scope="function", autouse=False)
def allure_steps(request, driver):
    screenshots_taken = []

    def take_step_screenshot(step_name):
        try:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=step_name,
                attachment_type=allure.attachment_type.PNG
            )
            screenshots_taken.append(step_name)
        except Exception as e:
            print(f"Erro ao capturar screenshot em '{step_name}': {e}")

    driver.allure_screenshot = take_step_screenshot
    yield

    if screenshots_taken:
        allure.attach(
            f"Screenshots capturadas: {len(screenshots_taken)}\n" + "\n".join(screenshots_taken),
            name="log_screenshots",
            attachment_type=allure.attachment_type.TEXT
        )

@pytest.fixture(scope="function", autouse=False)
def allure_auto_steps(request, driver):
    screenshot_count = [0]  

    def auto_screenshot(prefix="step"):
        screenshot_count[0] += 1
        try:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=f"{prefix}_{screenshot_count[0]:02d}",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Erro ao capturar screenshot: {e}")

    driver.screenshot = auto_screenshot
    yield

def pytest_configure(config):
    if not hasattr(config.option, 'allure_report_dir') or not config.option.allure_report_dir:
        config.option.allure_report_dir = "allure-results"

