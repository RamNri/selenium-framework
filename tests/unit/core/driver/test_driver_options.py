import pytest

from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions

from core.driver.driver_options import DriverOptions
from core.driver.browser import Browser


def test_chrome_headless():
  options = DriverOptions.create(Browser.CHROME, headless=True,)
  assert isinstance(options, ChromeOptions,)

  assert "--headless=new" in options.arguments
  assert "--start-maximized" in options.arguments

def test_chrome_non_headless():
  options = DriverOptions.create(Browser.CHROME, headless=False,)
  assert isinstance(options, ChromeOptions,)

  assert "--headless=new" not in options.arguments
  assert "--start-maximized" in options.arguments

def test_firefox_headless():
  options = DriverOptions.create(Browser.FIREFOX, headless=True,)
  assert isinstance(options, FirefoxOptions)

  assert "--headless" in options.arguments
  assert "--start-maximized" in options.arguments

def test_firefox_non_headless():
  options = DriverOptions.create(Browser.FIREFOX, headless=False,)
  assert isinstance(options, FirefoxOptions)

  assert "--headless" not in options.arguments
  assert "--start-maximized" in options.arguments

def test_edge_headless():
  options = DriverOptions.create(Browser.EDGE, headless=True,)
  assert isinstance(options, EdgeOptions)

  assert "--headless=new" in options.arguments
  assert "--start-maximized" in options.arguments

def test_edge_non_headless():
  options = DriverOptions.create(Browser.EDGE, headless=False,)
  assert isinstance(options, EdgeOptions)

  assert "--headless=new" not in options.arguments
  assert "--start-maximized" in options.arguments

def test_unsupported_browser():
  with pytest.raises(ValueError):
    DriverOptions.create("safari", headless=False,)