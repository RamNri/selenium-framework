import logging

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import settings

from core.driver.browser import Browser
from core.driver.driver_options import DriverOptions
from core.execution.execution_context import ExecutionContext


logger = logging.getLogger(__name__)


# ============================================================
# Browser creator functions
# ============================================================

def _create_chrome(options):

    return webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        ),
        options=options,
    )


def _create_firefox(options):

    return webdriver.Firefox(
        service=FirefoxService(
            GeckoDriverManager().install()
        ),
        options=options,
    )


def _create_edge(options):

    return webdriver.Edge(
        service=EdgeService(
            EdgeChromiumDriverManager().install()
        ),
        options=options,
    )


# ============================================================
# Driver Factory
# ============================================================

class DriverFactory:

    _CREATORS = {
        Browser.CHROME: _create_chrome,
        Browser.FIREFOX: _create_firefox,
        Browser.EDGE: _create_edge,
    }

    @staticmethod
    def create():

        browser = Browser(
            settings.BROWSER.lower()
        )

        options = DriverOptions.create(
            browser,
            settings.HEADLESS,
        )

        creator = DriverFactory._CREATORS[browser]

        driver = creator(options)

        ExecutionContext.set_driver(driver)
        ExecutionContext.set_browser(browser.value)
        ExecutionContext.set_session_id(driver.session_id)

        logger.info(
            "Browser created : %s",
            browser.value,
        )

        logger.info(
            "Session Id : %s",
            driver.session_id,
        )

        return driver

    @staticmethod
    def current():

        return ExecutionContext.driver()

    @staticmethod
    def quit():

        driver = ExecutionContext.driver()

        if driver is None:
            return

        logger.info(
            "Closing browser session %s",
            driver.session_id,
        )

        driver.quit()

        ExecutionContext.set_driver(None)
        ExecutionContext.set_browser(None)
        ExecutionContext.set_session_id(None)