from selenium.webdriver import ChromeOptions

class BrowserOption:
  
  @staticmethod
  def chrome():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("disable-notification")

    return options