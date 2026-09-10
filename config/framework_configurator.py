from config.environment_manager import EnvironmentManager
from config.runtime_manager import RuntimeManager
from config import settings

class FrameworkConfigurator:

  @staticmethod
  def configure(environment: str, browser: str, headless: bool, execution_mode: str,):
    #Build and validate everything first

    environment_config = EnvironmentManager.build(environment)
    runtime_config = RuntimeManager.build(browser=browser,
                                          headless=headless, 
                                          execution_mode=execution_mode, 
                                          grid_url=settings.GRID_URL)

    #Apply only after everything is valid
    EnvironmentManager.apply(environment_config)
    RuntimeManager.apply(runtime_config)


   