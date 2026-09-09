from config import settings
from config.environment import EnvironmentResolver
from core.exceptions import ConfigurationException
import pytest
from config.environment_config import EnvironmentConfig

class TestEnvironmentConfiguration:

  def test_resolver_returns_requested_environment(self):
    resolver = EnvironmentResolver()
    assert resolver.resolve("qa") == "qa"

  def test_resolver_rejects_invalid_environment(self):
    resolver = EnvironmentResolver()

    with pytest.raises(ConfigurationException):
      resolver.resolve("invalid")

  def test_resolver_rejects_empty_environment(self):
    resolver = EnvironmentResolver()

    with pytest.raises(ConfigurationException):
      resolver.resolve("")

  def test_resolver_defaults_to_local(self):
    resolver = EnvironmentResolver()

    assert resolver.resolve() == "local"

  def test_environment_option_updates_settings(self, pytestconfig):
    assert settings.ENVIRONMENT == pytestconfig.getoption("--env")

  def test_environment_config_contains_local_url(self):
    config = EnvironmentConfig("local")
    assert config.base_url == "https://www.saucedemo.com"
    assert config.api_base_url == "https://restful-booker.herokuapp.com"

  def test_environment_config_rejects_invalid_environment(self):
    with pytest.raises(ConfigurationException):
        EnvironmentConfig("invalid")

  def test_environment_config_provides_urls(self, pytestconfig):
    environment = pytestconfig.getoption("--env")
    environment_config = EnvironmentConfig(environment)

    assert settings.BASE_URL == environment_config.base_url
    assert settings.API_BASE_URL == environment_config.api_base_url   