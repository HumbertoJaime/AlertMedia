from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_amazon_login_page(open_amazon):
    home_page = open_amazon 
    login_page = home_page.go_to_login_page()
    login_page.fill_email("humberto.edpo@gmail.com")
    login_page.click_continue_button()
    expected_title = "Amazon Iniciar sesión"
    WebDriverWait(login_page.driver, 10).until(
        EC.title_is(expected_title)
    )
    assert login_page.driver.title == expected_title, f"Error: El título esperado era '{expected_title}' pero se encontró '{login_page.driver.title}'"

