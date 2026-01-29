# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    """Fixture que cria e configura o driver"""
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
    yield driver  # Retorna o driver para os testes
    driver.quit()  # Fecha o driver após os testes

@pytest.fixture
def wait(driver):
    """Fixture para WebDriverWait"""
    return WebDriverWait(driver, 10)

# ========== FIXTURES DE DADOS DE TESTE ==========

@pytest.fixture
def valid_credentials():
    """Retorna credenciais válidas para login"""
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }

@pytest.fixture
def invalid_credentials():
    """Retorna credenciais inválidas"""
    return {
        "username": "invalid_user",
        "password": "wrong_password"
    }

@pytest.fixture
def locked_user_credentials():
    """Retorna credenciais de usuário bloqueado"""
    return {
        "username": "locked_out_user",
        "password": "secret_sauce"
    }

@pytest.fixture
def problem_user_credentials():
    """Retorna credenciais de usuário com problemas"""
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
    """Parametriza teste com múltiplos usuários válidos"""
    return {
        "username": request.param[0],
        "password": request.param[1]
    }

# Executar login -----------------------------------------

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

# ------------ Dados do Usuário Checkout -----------------

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

# ========== INTEGRAÇÃO ALLURE PARA TESTES E2E ==========

import allure
import os

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar resultado do teste e anexar screenshot em falhas"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    # Captura screenshot apenas para testes E2E em caso de falha
    if rep.when == "call" and rep.failed:
        if "test_e2e" in item.nodeid:  # Aplica apenas ao test_e2e.py
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
def allure_e2e_steps(request, driver):
    """Fixture para capturar screenshots automaticamente em cada etapa do E2E"""
    # Aplica apenas para testes que contenham 'test_e2e' no nome
    if "test_e2e" not in request.node.nodeid:
        yield
        return

    screenshots_taken = []

    def take_step_screenshot(step_name):
        """Captura screenshot e anexa ao Allure"""
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

    # Disponibiliza a função para uso manual se necessário
    driver.allure_screenshot = take_step_screenshot

    yield

    # Log de quantas screenshots foram capturadas
    if screenshots_taken:
        allure.attach(
            f"Screenshots capturadas: {len(screenshots_taken)}\n" + "\n".join(screenshots_taken),
            name="log_screenshots",
            attachment_type=allure.attachment_type.TEXT
        )

def pytest_configure(config):
    """Configura metadados do Allure para testes E2E"""
    # Define diretório de resultados Allure se não existir
    if not config.option.allure_report_dir:
        config.option.allure_report_dir = "allure-results"

