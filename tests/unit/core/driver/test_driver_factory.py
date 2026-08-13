from unittest.mock import Mock, patch

from core.driver.browser import Browser
from core.driver.driver_factory import DriverFactory


class TestDriverFactory:

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_driver"
    )
    @patch(
        "core.driver.driver_factory.DriverOptions.create"
    )
    @patch(
        "core.driver.driver_factory.settings"
    )
    def test_create_chrome(
        self,
        settings,
        options_create,
        set_driver,
    ):

        # Arrange
        settings.BROWSER = "chrome"
        settings.HEADLESS = False

        fake_options = Mock()
        options_create.return_value = fake_options

        fake_driver = Mock()
        fake_driver.session_id = "chrome-session-123"

        fake_creator = Mock(return_value=fake_driver)

        with patch.dict(
            DriverFactory._CREATORS,
            {
              Browser.CHROME: fake_creator },
        ):
            # Act
            driver = DriverFactory.create()

        # Assert
        assert driver is fake_driver

        options_create.assert_called_once_with(
            Browser.CHROME,
            False,
        )

        fake_creator.assert_called_once_with(
            fake_options,
        )

        set_driver.assert_called_once_with(
            fake_driver,
        )

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_driver"
    )
    @patch(
        "core.driver.driver_factory.DriverOptions.create"
    )
    @patch(
        "core.driver.driver_factory.settings"
    )
    def test_create_firefox(
        self,
        settings,
        options_create,
        set_driver,
    ):

        # Arrange
        settings.BROWSER = "firefox"
        settings.HEADLESS = False

        fake_options = Mock()
        options_create.return_value = fake_options

        fake_driver = Mock()
        fake_driver.session_id = "firefox-session-123"

        fake_creator = Mock(
            return_value=fake_driver
        )

        with patch.dict(
            DriverFactory._CREATORS,
            {
                Browser.FIREFOX: fake_creator
            },
        ):

            # Act
            driver = DriverFactory.create()

        # Assert
        assert driver is fake_driver

        options_create.assert_called_once_with(
            Browser.FIREFOX,
            False,
        )

        fake_creator.assert_called_once_with(
            fake_options,
        )

        set_driver.assert_called_once_with(
            fake_driver,
        )

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_driver"
    )
    @patch(
        "core.driver.driver_factory.DriverOptions.create"
    )
    @patch(
        "core.driver.driver_factory.settings"
    )
    def test_create_edge(
        self,
        settings,
        options_create,
        set_driver,
    ):

        # Arrange
        settings.BROWSER = "edge"
        settings.HEADLESS = False

        fake_options = Mock()
        options_create.return_value = fake_options

        fake_driver = Mock()
        fake_driver.session_id = "edge-session-123"

        fake_creator = Mock(
                    return_value=fake_driver
                )

        with patch.dict(
            DriverFactory._CREATORS,
            {
                Browser.EDGE: fake_creator
            },
        ):

            # Act
            driver = DriverFactory.create()

        # Assert
        assert driver is fake_driver

        options_create.assert_called_once_with(
            Browser.EDGE,
            False,
        )

        fake_creator.assert_called_once_with(
            fake_options,
        )

        set_driver.assert_called_once_with(
            fake_driver,
        )

    @patch(
        "core.driver.driver_factory.ExecutionContext.driver"
    )
    def test_current_driver(
        self,
        current_driver,
    ):

        # Arrange
        fake_driver = Mock()

        current_driver.return_value = fake_driver

        # Act
        result = DriverFactory.current()

        # Assert
        assert result is fake_driver

        current_driver.assert_called_once()

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_driver"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.driver"
    )
    def test_quit_driver(
        self,
        current_driver,
        set_driver,
    ):

        # Arrange
        fake_driver = Mock()
        fake_driver.session_id = "session-123"

        current_driver.return_value = fake_driver

        # Act
        DriverFactory.quit()

        # Assert
        fake_driver.quit.assert_called_once()

        set_driver.assert_called_once_with(None)

    @patch(
        "core.driver.driver_factory.ExecutionContext.driver"
    )
    def test_quit_without_driver(
        self,
        current_driver,
    ):

        # Arrange
        current_driver.return_value = None

        # Act
        DriverFactory.quit()

        # Assert
        current_driver.assert_called_once()

    def test_all_browsers_are_registered(self):

        assert Browser.CHROME in DriverFactory._CREATORS
        assert Browser.FIREFOX in DriverFactory._CREATORS
        assert Browser.EDGE in DriverFactory._CREATORS