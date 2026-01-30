from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
import allure

@allure.epic("Testes E2E")
@allure.feature("Fluxo Completo de Compra")
@allure.story("Jornada de Usuário - Login até Finalização do Pedido")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("e2e", "smoke", "regression", "purchase-flow")
@allure.description("""
### 🎯 Objetivo do Teste
Validar o fluxo completo de compra end-to-end desde a autenticação até a conclusão do pedido,
garantindo que todos os processos críticos de negócio funcionem corretamente de forma integrada.

### 📋 Cenário BDD

**Dado que** um usuário possui credenciais válidas e acessa a página de login  
**E** existem produtos disponíveis no inventário  
**Quando** o usuário faz login com suas credenciais  
**E** adiciona 2 produtos ao carrinho de compras  
**E** navega para o carrinho e inicia o processo de checkout  
**E** preenche as informações obrigatórias (nome, sobrenome e CEP)  
**E** confirma a finalização da compra  
**Então** o pedido deve ser concluído com sucesso  
**E** a página de confirmação deve ser exibida

### ✅ Critérios de Sucesso
- Autenticação bem-sucedida com redirecionamento para página de inventário
- Badge do carrinho exibe contagem correta de 2 produtos
- Navegação fluida por todas as etapas do checkout
- Página de conclusão do pedido alcançada e validada
""")
class TestE2E:

    @allure.title("Fluxo completo de compra - Login até conclusão do pedido")
    def test_complete_purchase_flow(self, driver, valid_credentials, data_checkout, allure_auto_steps):
        """Teste E2E: Valida jornada completa do usuário realizando uma compra com sucesso."""

        with allure.step("Dado que o usuário acessa a página de login"):
            login_page = LoginPage(driver)
            login_page.navigate_to_login()
            driver.screenshot()

        with allure.step("Quando o usuário faz login com credenciais válidas"):
            login_page.login(valid_credentials["username"], valid_credentials["password"])
            driver.screenshot()

        with allure.step("Então o usuário deve ser redirecionado para a página de inventário"):
            assert "inventory.html" in driver.current_url
            driver.screenshot()

        with allure.step("Quando o usuário adiciona 2 produtos ao carrinho"):
            products_page = ProductsPage(driver)
            products_page.add_product(0)
            products_page.add_product(2)
            driver.execute_script("window.scrollTo(0, 0);")
            driver.screenshot()

        with allure.step("Então o badge do carrinho deve exibir 2 itens"):
            assert products_page.get_cart_badge_count() == 2

        with allure.step("Quando o usuário navega para o carrinho de compras"):
            checkout_page = CheckoutPage(driver)
            checkout_page.navigate_shopping_cart_link()
            driver.screenshot()

        with allure.step("E inicia o processo de checkout"):
            checkout_page.click_checkout()
            driver.screenshot()

        with allure.step("E preenche as informações obrigatórias do cliente"):
            checkout_page.fill_first_name(data_checkout["first_name"])
            checkout_page.fill_last_name(data_checkout["last_name"])
            checkout_page.fill_postal_code(data_checkout["postal_code"])
            driver.screenshot()

        with allure.step("E avança para a revisão do pedido"):
            checkout_page.click_continue()
            driver.screenshot()

        with allure.step("E confirma a finalização da compra"):
            checkout_page.click_finish()
            driver.screenshot()

        with allure.step("Então a página de conclusão do pedido deve ser exibida"):
            assert "checkout-complete.html" in driver.current_url
            driver.screenshot()
