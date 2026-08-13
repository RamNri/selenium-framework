from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions

from core.driver.browser import Browser

class DriverOptions:

  @staticmethod
  def create(browser: Browser, headless: bool):
    if browser == Browser.CHROME:
      options = ChromeOptions()
    elif browser == Browser.FIREFOX:
      options = FirefoxOptions()
    else:
      options = EdgeOptions()

    if headless:
      options.add_argument("--headless=new")

    options.add_argument("--start-maximized")

    return options