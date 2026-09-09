from config.environment_manager import EnvironmentManager
from config.runtime_manager import RuntimeManager

class FrameworkConfigurator:

  @staticmethod
  def configure(environment: str, browser: str, headless: bool,):
    #Build and validate everything first

    environment_config = EnvironmentManager.build(environment,)
    runtime_config = RuntimeManager.build(browser=browser, headless=headless,)

    #Apply only after everything is valid
    EnvironmentManager.apply(environment_config)
    RuntimeManager.apply(runtime_config)


   