from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions

from core.driver.browser import Browser

class DriverOptions:
  def create(browser:Browser, headless: bool):
    if browser == Browser.CHROME:
      options = ChromeOptions()

      if headless:
        options.add_argument("--headless=new")
    elif browser == Browser.FIREFOX:
      options = FirefoxOptions()

      if headless:
        options.add_argument("--headless")
    elif browser == Browser.EDGE:
      options = EdgeOptions()

      if headless:
        options.add_argument("--headless=new")
    else:
      raise ValueError(
        f"unsupported browser: {browser}"
      )

    options.add_argument("--start-maximized")

    return options
        

    
