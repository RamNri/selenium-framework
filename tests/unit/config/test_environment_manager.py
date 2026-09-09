from config import settings
from config.environment_manager import EnvironmentManager

class TestEnviromentManager:
  def test_configure_qa_environment_updates_settings(self):
    EnvironmentManager.configure("qa")

    assert settings.ENVIRONMENT == "qa"
    assert settings.BASE_URL == "https://www.saucedemo.com"
    assert settings.API_BASE_URL == "https://restful-booker.herokuapp.com"