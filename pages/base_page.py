import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from core.exceptions import ElementNotFoundError

logger = logging.getLogger(__name__)


class BasePage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)

  def find(self, locator):
    logger.info("Finding element %s", locator)
    try:

      return self.wait.until(EC.visibility_of_element_located(locator))
    except TimeoutException as exc:

      logger.error("Failed to locate element %s", locator)

      raise ElementNotFoundError(
        locator=locator,
        page_name=self.__class__.__name__,
        timeout=self.wait._timeout,
        current_url=self.driver.current_url,
        page_title=self.driver.title,
      ) from exc

  
  def find_all(self, locator):
    try:
      return self.wait.until(EC.visibility_of_all_elements_located(locator))
    except TimeoutException as exc:

      raise ElementNotFoundError(
        locator=locator,
                page_name=self.__class__.__name__,
                timeout=self.wait._timeout,
                current_url=self.driver.current_url,
                page_title=self.driver.title,
      ) from exc
  
  def click(self, locator):
    logger.info("clicking element %s", locator)
    self.find(locator).click()
  
  def type(self, locator, text):
    logger.info("Typing info %s", locator)
    element = self.find(locator)
    element.clear()
    element.send_keys(text)

  def get_text(self, locator):
    logger.info("Getting text from element %s", locator)
    return self.find(locator).text
    