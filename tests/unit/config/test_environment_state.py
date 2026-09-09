from config import settings
from config.environment_manager import EnvironmentManager

class TestEnvironmentState:
  def test_environment_configuration_can_be_changed(self, preserve_environment_settings,):
    EnvironmentManager.configure("qa")
    assert settings.ENVIRONMENT ==  "qa"

  def test_environment_configuration_can_be_reset_to_local(self, preserve_environment_settings,):
    EnvironmentManager.configure("qa")
    assert settings.ENVIRONMENT == "qa"

    EnvironmentManager.configure("local")
    assert settings.ENVIRONMENT == "local"