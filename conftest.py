import pytest
from selenium import webdriver
from pathlib import Path
from datetime import datetime
from core.driver_factory import DriverFactory
from core.logger import configure_logging
from pytest_html import extras

configure_logging()


@pytest.fixture
def driver(request):  
  #request is pytest object that contains info about the current test session
  #one of the things is the command-line configuration
  #driver = webdriver.Chrome()
  browser = request.config.getoption("--browser")
  driver = DriverFactory.create_driver(browser)

  yield driver
  
  driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
  outcome = yield
  report = outcome.get_result()

  if report.when == "call":
    if report.failed:
      driver = item.funcargs.get("driver")
      if driver is None:
        return
      screenshot_dir = (
        Path("artifacts")/"screenshots" / item.name
      )

      screenshot_dir.mkdir(parents=True, exist_ok=True)
      timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
      filename = (f"{item.name}_{timestamp}.png")
      filepath = (screenshot_dir/filename)
      driver.save_screenshot(str(filepath))
      extra = getattr(report, "extras", [])
      extra.append(extras.image(str(filepath)))
      report.extras = extra
 
def pytest_addoption(parser):
    
    parser.addoption(
      "--browser",
      action="store",
      default="chrome",
      help="Brower to run tests on"
    )

"""
#But we are going to discuss teardown safety, 
fixture scope, 
command-line browser selection, 
headless execution, 
failure screenshots, 
config, 
parallel workers and 
driver isolation.
"""