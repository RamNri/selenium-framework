from config import settings
from config.framework_configurator import FrameworkConfigurator
from core.exceptions import ConfigurationException
import pytest

class TestFrameworkConfigurator:
  def test_configure_updates_environment_settings(
      self,
      preserve_environment_settings, preserve_runtime_settings
  ):
    FrameworkConfigurator.configure(
      environment="qa",
      browser="chrome",
      headless=False,
    )

    assert settings.ENVIRONMENT == "qa"

  def test_configure_updates_runtime_settings(
      self,
      preserve_environment_settings,
      preserve_runtime_settings
  ):
    FrameworkConfigurator.configure(
      environment = "local",
      browser="firefox",
      headless=True
    )
    assert settings.BROWSER == "firefox"
    assert settings.HEADLESS is True

  def test_configure_updates_complete_framework_state(
      self,
      preserve_environment_settings,
      preserve_runtime_settings
  ):
    FrameworkConfigurator.configure(
      environment="qa",
      browser="edge",
      headless=True,
    )

    assert settings.ENVIRONMENT == "qa"
    assert settings.BROWSER == "edge"
    assert settings.HEADLESS is True

  def test_configure_rejects_invalid_environment(
      self,
      preserve_environment_settings,
      preserve_runtime_settings
  ):
    with pytest.raises(ConfigurationException):
      FrameworkConfigurator.configure(
        environment="invalid",
        browser="chrome",
        headless=False,
      )

  def test_configure_rejects_invalid_browser(
      self,
      preserve_environment_settings,
      preserve_runtime_settings
  ):
    with pytest.raises(ConfigurationException):
      FrameworkConfigurator.configure(
        environment="local",
        browser="invalid",
        headless=False
      )

  def test_configuration_failure_does_not_leave_partial_state(
    self,
    preserve_environment_settings,
    preserve_runtime_settings
  ):
    original_environment = settings.ENVIRONMENT
    original_base_url = settings.BASE_URL
    original_api_base_url = settings.API_BASE_URL
    original_browser = settings.BROWSER
    original_headless = settings.HEADLESS

    with pytest.raises(ConfigurationException):
      FrameworkConfigurator.configure(
        environment="qa",
        browser="invalid",
        headless=True,
      )

    assert settings.ENVIRONMENT == original_environment
    assert settings.BASE_URL == original_base_url
    assert settings.API_BASE_URL == original_api_base_url

    assert settings.BROWSER == original_browser
    assert settings.HEADLESS == original_headless