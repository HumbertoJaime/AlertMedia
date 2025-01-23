import pytest
from selenium.webdriver.common.by import By

def test_amazon_home_page_title(open_amazon):
    home_page = open_amazon 
    title = home_page.driver.title  
    assert "Amazon" in title

def test_get_search_textbox(open_amazon):
    home_page = open_amazon
    searchbox = home_page.driver.find_element(By.ID,"twotabsearchtextbox")
    assert searchbox is not None
   
def test_get_search_loop_icon(open_amazon):
    home_page = open_amazon
    searchbox = home_page.driver.find_element(By.ID,"nav-search-submit-button")
    assert searchbox is not None

def test_search_item(open_amazon):
    home_page = open_amazon
    home_page.search_item("Laptop")
    assert "laptop" in home_page.driver.title.lower()
    