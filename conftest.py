import pytest

from pathlib import Path
from datetime import datetime

from config import settings

from core.driver.driver_factory import DriverFactory
from core.logger import configure_logging

from pytest_html import extras
from core.execution.execution_context import ExecutionContext


configure_logging()


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on",
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )


@pytest.fixture
def driver(request):

    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    # Command-line browser selection overrides
    # the default framework configuration for this run.
    settings.BROWSER = browser
    settings.HEADLESS = headless

    driver = DriverFactory.create()

    yield driver

    DriverFactory.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    worker_id = getattr(item.config, "workerinput", {},).get("workerid", "master",)
    ExecutionContext.set_worker_id(worker_id)
    ExecutionContext.set_test_name(item.nodeid)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when != "call":
        return

    if not report.failed:
        return

    driver = item.funcargs.get("driver")

    if driver is None:
        return

    screenshot_dir = (
        Path("artifacts")
        / "screenshots"
        / item.name
    )

    screenshot_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"{item.name}_{timestamp}.png"
    )

    filepath = screenshot_dir / filename

    driver.save_screenshot(
        str(filepath)
    )

    extra = getattr(
        report,
        "extras",
        [],
    )

    extra.append(
        extras.image(
            str(filepath)
        )
    )

    report.extras = extra