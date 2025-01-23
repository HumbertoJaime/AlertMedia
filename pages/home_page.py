from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
    
    def search_item(self, item):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox") 
        search_box.clear()
        search_box.send_keys(item)
        search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()
    

