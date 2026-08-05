from selenium import webdriver
from core.browser_options import BrowserOption


class DriverFactory:
  

  @staticmethod
  def create_driver(browser):

    BROWSERS = {
    "chrome": webdriver.Chrome,
    "firefox": webdriver.Firefox,
    "edge":webdriver.Edge
  }
    
    options = BrowserOption.chrome()

    driver_class = BROWSERS.get(browser)

    if driver_class is None:
      raise ValueError(
      f"Unsupported browser: {browser}"
    )

    return driver_class(options)
  
