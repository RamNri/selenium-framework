from core.exceptions import ConfigurationException

class EnvironmentConfig:

  ENVIRONMENTS = {
    "local" :{
      "base_url" : "https://www.saucedemo.com",
      "api_base_url": "https://restful-booker.herokuapp.com",
    },
    "qa" : {
      "base_url" : "https://www.saucedemo.com",
      "api_base_url" : "https://restful-booker.herokuapp.com",
    },
    "staging" : {
      "base_url" : "https://www.saucedemo.com",
      "api_base_url" : "https://restful-booker.herokuapp.com",
    },

  }

  def __init__(self, environment: str):

    if environment not in self.ENVIRONMENTS:
      raise ConfigurationException(
        f"Unsupported Environment: '{environment}'"
      )
    
    self.environment = environment

    config = self.ENVIRONMENTS[environment]
    
    self.base_url = config["base_url"]
    self.api_base_url = config["api_base_url"]
