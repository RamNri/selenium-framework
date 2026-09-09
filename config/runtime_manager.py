from config import settings
from core.driver.browser import Browser
from core.exceptions import ConfigurationException

class RuntimeManager:

  @staticmethod
  def build(browser: str, headless: bool):
    try:
      resolved_browser = Browser(browser.lower())
    except ValueError as ex:
      raise ConfigurationException(
        f"Unsupported browser: '{browser}'"
      ) from ex

    return {
      "browser": resolved_browser.value,
      "headless": headless,
    }

  @staticmethod
  def apply(runtime_config):
    settings.BROWSER = runtime_config["browser"]
    settings.HEADLESS = runtime_config["headless"]

  @staticmethod
  def configure(browser:str, headless: bool):
    runtime_config = RuntimeManager.build(browser=browser, headless=headless)
    RuntimeManager.apply(runtime_config)
  