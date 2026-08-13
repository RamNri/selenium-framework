from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
  TITLE = (By.CLASS_NAME, "title")

  def __init__(self, driver):
    super().__init__(driver)

  def get_title(self):
    return self.find(self.TITLE).text
  
  def is_loaded(self):
    return self.get_title() == "Products"
  
