from config import settings
from config.environment import EnvironmentResolver
from config.environment_config import EnvironmentConfig

class EnvironmentManager:

  @staticmethod
  def build(environment: str = "local") -> EnvironmentConfig:
    resolved_environment = EnvironmentResolver().resolve(environment)
    return EnvironmentConfig(resolved_environment)

  @staticmethod
  def apply(environment_config: EnvironmentConfig):

    settings.ENVIRONMENT = environment_config.environment
    settings.BASE_URL = environment_config.base_url
    settings.API_BASE_URL = environment_config.api_base_url

  @staticmethod
  def configure(environment: str = "local"):
    environment_config = EnvironmentManager.build(environment)
    EnvironmentManager.apply(environment_config)