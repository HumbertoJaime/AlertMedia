from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def fill_email(self,email):
        email_field = self.driver.find_element(By.CSS_SELECTOR, '[type="email"]')
        email_field.send_keys(email)

    
    def click_continue_button(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    

    
    