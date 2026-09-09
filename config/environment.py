from core.exceptions import ConfigurationException
class EnvironmentResolver:

  SUPPORTED_ENVIRONMENTS = {
    "local",
    "qa",
    "staging"
  }
 
  def resolve(self, environment: str = "local") -> str:
    if environment not in self.SUPPORTED_ENVIRONMENTS:
      raise ConfigurationException(
        f"Unsupported Environment: '{environment}'"
      )

    return environment