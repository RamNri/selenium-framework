import pytest
from config import settings

@pytest.fixture
def preserve_environment_settings():
  original_environment = settings.ENVIRONMENT
  original_base_url = settings.BASE_URL
  original_api_base_url = settings.API_BASE_URL

  yield

  settings.ENVIRONMENT = original_environment
  settings.BASE_URL = original_base_url
  settings.API_BASE_URL = original_api_base_url

@pytest.fixture
def preserve_runtime_settings():
  original_browser = settings.BROWSER
  original_headless = settings.HEADLESS

  yield

  settings.BROWSER = original_browser
  settings.HEADLESS = original_headless