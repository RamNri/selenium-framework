from config import settings
from core.driver.browser import Browser
from core.exceptions import ConfigurationException
from core.driver.execution_mode import ExecutionMode

class RuntimeManager:

  @staticmethod
  def build(browser: str, 
            headless: bool,
            execution_mode:str,
            grid_url:str,
            ):
    try:
      resolved_browser = Browser(browser.lower())
      execution_mode_value= ExecutionMode(execution_mode).value
      
    except ValueError as ex:
      raise ConfigurationException(
        f"Unsupported runtime configuration"
      ) from ex

    return {
      "browser": resolved_browser.value,
      "headless": headless,
      "execution_mode": execution_mode_value,
      "grid_url": grid_url
    }
  
  @staticmethod
  def apply(runtime_config):
    settings.BROWSER = runtime_config["browser"]
    settings.HEADLESS = runtime_config["headless"]
    settings.EXECUTION_MODE = runtime_config["execution_mode"]
    settings.GRID_URL = runtime_config["grid_url"]

  @staticmethod
  def configure(browser:str, 
                headless: bool,
                execution_mode: str = settings.EXECUTION_MODE,
                grid_url: str = settings.GRID_URL,):
    runtime_config = RuntimeManager.build(browser=browser, 
                                          headless=headless,
                                          execution_mode=execution_mode,
                                          grid_url=grid_url,)
    RuntimeManager.apply(runtime_config)
  