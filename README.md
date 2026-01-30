# 🧪 SauceDemo Test Automation
Projeto de automação de testes end-to-end para SauceDemo utilizando Python, Pytest, Selenium WebDriver e Page Object Model (POM). Desenvolvido como portfólio de QA Engineer, demonstrando habilidades em automação web, design patterns e boas práticas de desenvolvimento.


## 🎯 Funcionalidades Testadas
- ✅ Autenticação (login/logout) e testes de usuários bloqueados
- ✅ Navegação, ordenação e listagem de produtos
- ✅ Gerenciamento do carrinho (adição/remoção de itens)
- ✅ Validação de badges e contadores
- ✅ Fluxo completo de checkout e finalização de compra
- ✅ Testes negativos (credenciais inválidas, usuários bloqueados)

## 🛠️ Stack Tecnológica
| Tecnologia         | Finalidade                     |
| ------------------ | ------------------------------ |
| Python 3.x         | Linguagem principal            |
| Selenium WebDriver | Automação de navegadores       |
| Pytest             | Framework de testes            |
| Allure Report      | Relatórios interativos         |
| POM Pattern        | Organização e manutenibilidade |
## 🚀 Instalação e Execução
### Pré-requisitos
- Python 3.8+
- Chrome ou Firefox
- pip
### Setup
``` 
# Clone o repositório
git clone https://github.com/daniloabramo/saucedemo-test-automation.git
cd saucedemo-test-automation

# Instale as dependências
pip install -r requirements.txt
```
### Executar Testes
```
# Todos os testes
pytest tests/

# Teste específico
pytest tests/test_login.py

# Com relatório Allure
pytest --alluredir=reports/
allure serve reports/
 ```
## 📊 Relatórios Allure
Os relatórios incluem:
- Status de execução detalhado
- Screenshots automáticos em falhas
- Logs de cada passo do teste
- Métricas de tempo e tendências
- Visualização interativa de resultados 

<details>
<summary>Print do Relatório Allure Fluxo E2E</summary>
<img src="imgs/print-allure.png" alt="Relatório Allure">
</details>

## Padrão Page Object Model
Cada página possui uma classe dedicada com métodos para interação, promovendo:
- Reusabilidade de código
- Manutenibilidade facilitada
- Separação entre lógica de teste e interação com elementos
- Redução de código duplicado

### Exemplo de Implementação
**BasePage** - Classe base com métodos comuns (waits, badges, remoção de produtos)<br>
**LoginPage** - Autenticação e navegação inicial<br>
**ProductsPage** - Adição de produtos ao carrinho<br>
**CheckoutPage** - Fluxo completo de finalização de compra
# 🎓 Aprendizados e Diferenciais
- Automação robusta com Selenium WebDriver e explicit waits
- Implementação prática de design pattern POM
- Testes parametrizados com pytest fixtures
- Integração de screenshots automáticos no Allure
- Organização profissional de projetos de teste
- Boas práticas de desenvolvimento em Python
## 🔍 Cenários de Teste
### Login
- Login com múltiplos usuários válidos (standard, problem, performance_glitch)
- Validação de usuário bloqueado (locked_out_user)
- Testes negativos com credenciais inválidas
### Shopping Flow
- Adição/remoção de múltiplos produtos
- Validação de contadores de badge
- Navegação entre páginas
### Checkout
- Preenchimento dos dados do comprador
- Validação de URLs em cada etapa
### E2E
- Fluxo completo: login → adicionar produtos → checkout → confirmação
- Preenchimento de formulário de informações
- Teste crítico com Allure steps detalhados

## 📧 Contato
https://br.linkedin.com/in/danilo-abramo <br>
daniloabramowicz@gmail.com
