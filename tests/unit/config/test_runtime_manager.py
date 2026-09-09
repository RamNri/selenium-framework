from config import settings
from config.runtime_manager import RuntimeManager
from core.exceptions import ConfigurationException
import pytest


class TestRuntimeManager:

  def test_configure_browser_updates_settings(self, preserve_runtime_settings,):
    RuntimeManager.configure(browser="firefox", headless=False,)
    assert settings.BROWSER == "firefox"

  def test_configure_headless_updates_settings(self, preserve_runtime_settings):
    RuntimeManager.configure(
      browser="chrome",
      headless=True,
    )

    assert settings.HEADLESS is True

  def test_configure_runtime_updates_all_settings(self, preserve_runtime_settings):
    RuntimeManager.configure(
      browser="chrome",
      headless=True,
    )

    assert settings.HEADLESS is True

  def test_configure_runtime_updates_all_settings(self, preserve_runtime_settings,):
    RuntimeManager.configure(
      browser="edge",
      headless=True,
    )

    assert settings.BROWSER == "edge"
    assert settings.HEADLESS is True

  def test_configure_rejects_invalid_browser(self, preserve_runtime_settings,):
    with pytest.raises(ConfigurationException):
      RuntimeManager.configure(
        browser="test",
        headless=False,
      )

  def test_configure_normalizes_browser_name(self, preserve_runtime_settings,):
    RuntimeManager.configure(
      browser="CHROME",
      headless = False,
    )
    assert settings.BROWSER == 'chrome'