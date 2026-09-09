from unittest.mock import Mock, patch
import pytest
from core.driver.browser import Browser
from core.driver.driver_factory import DriverFactory


class TestDriverFactory:

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
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
    def test_create_chrome(
        self,
        settings,
        options_create,
        set_driver,
        set_browser,
        set_session_id,
    ):

        # Arrange
        settings.BROWSER = "chrome"
        settings.HEADLESS = False

        fake_options = Mock()
        options_create.return_value = fake_options

        fake_driver = Mock()
        fake_driver.session_id = "chrome-session-123"

        fake_creator = Mock(
            return_value=fake_driver
        )

        with patch.dict(
            DriverFactory._CREATORS,
            {
                Browser.CHROME: fake_creator
            },
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

        set_browser.assert_called_once_with(
            "chrome",
        )

        set_session_id.assert_called_once_with(
            "chrome-session-123",
        )

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
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
        set_browser,
        set_session_id,
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

        set_browser.assert_called_once_with(
            "firefox",
        )

        set_session_id.assert_called_once_with(
            "firefox-session-123",
        )

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
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
        set_browser,
        set_session_id,
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

        set_browser.assert_called_once_with(
            "edge",
        )

        set_session_id.assert_called_once_with(
            "edge-session-123",
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
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
    )
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
        set_browser,
        set_session_id,
    ):

        # Arrange
        fake_driver = Mock()
        fake_driver.session_id = "session-123"

        current_driver.return_value = fake_driver

        # Act
        DriverFactory.quit()

        # Assert
        fake_driver.quit.assert_called_once()

        set_driver.assert_called_once_with(
            None
        )

        set_browser.assert_called_once_with(
            None
        )

        set_session_id.assert_called_once_with(
            None
        )

    @patch(
        "core.driver.driver_factory.ExecutionContext.driver"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_driver"
    )
    def test_quit_without_driver(
        self,
        set_driver,
        set_browser,
        set_session_id,
        current_driver,
    ):

        # Arrange
        current_driver.return_value = None

        # Act
        DriverFactory.quit()

        # Assert
        current_driver.assert_called_once()

        set_driver.assert_not_called()
        set_browser.assert_not_called()
        set_session_id.assert_not_called()

    def test_all_browsers_are_registered(self):

        assert Browser.CHROME in DriverFactory._CREATORS
        assert Browser.FIREFOX in DriverFactory._CREATORS
        assert Browser.EDGE in DriverFactory._CREATORS

    @patch(
    "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
    "core.driver.driver_factory.ExecutionContext.set_browser"
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
    def test_create_does_not_publish_context_when_driver_creation_fails(
        self,
        settings,
        options_create,
        set_driver,
        set_browser,
        set_session_id,
    ):

        # Arrange
        settings.BROWSER = "chrome"
        settings.HEADLESS = False

        fake_options = Mock()

        options_create.return_value = fake_options

        fake_creator = Mock(
            side_effect=RuntimeError(
                "Browser failed to start"
            )
        )

        with patch.dict(
            DriverFactory._CREATORS,
            {
                Browser.CHROME: fake_creator
            },
        ):

            # Act / Assert
            with pytest.raises(
                RuntimeError,
                match="Browser failed to start",
            ):
                DriverFactory.create()

        # Assert

        fake_creator.assert_called_once_with(
            fake_options
        )

        set_driver.assert_not_called()

        set_browser.assert_not_called()

        set_session_id.assert_not_called()

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
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
    def test_create_does_not_publish_context_when_options_creation_fails(
        self,
        settings,
        options_create,
        set_driver,
        set_browser,
        set_session_id,
    ):

        # Arrange
        settings.BROWSER = "chrome"
        settings.HEADLESS = False

        options_create.side_effect = RuntimeError(
            "Driver options creation failed"
        )

        fake_creator = Mock()

        with patch.dict(
            DriverFactory._CREATORS,
            {
                Browser.CHROME: fake_creator
            },
        ):

            # Act / Assert
            with pytest.raises(
                RuntimeError,
                match="Driver options creation failed",
            ):
                DriverFactory.create()

        # Assert

        fake_creator.assert_not_called()

        set_driver.assert_not_called()

        set_browser.assert_not_called()

        set_session_id.assert_not_called()

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_driver"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.driver"
    )
    def test_quit_clears_execution_context_when_driver_quit_fails(
        self,
        current_driver,
        set_driver,
        set_browser,
        set_session_id,
    ):

        # Arrange
        fake_driver = Mock()
        fake_driver.session_id = "session-123"

        fake_driver.quit.side_effect = RuntimeError(
            "Browser shutdown failed"
        )

        current_driver.return_value = fake_driver

        # Act / Assert
        with pytest.raises(
            RuntimeError,
            match="Browser shutdown failed",
        ):
            DriverFactory.quit()

        # Assert
        set_driver.assert_called_once_with(None)

        set_browser.assert_called_once_with(None)

        set_session_id.assert_called_once_with(None)

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
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
    def test_create_uses_runtime_browser_configuration(
        self,
        settings,
        options_create,
        set_driver,
        set_browser,
        set_session_id,
    ):

        # Arrange
        settings.BROWSER = "firefox"
        settings.HEADLESS = True

        fake_options = Mock()
        options_create.return_value = fake_options

        fake_driver = Mock()
        fake_driver.session_id = "session-123"

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
            DriverFactory.create()

        # Assert
        options_create.assert_called_once_with(
            Browser.FIREFOX,
            True,
        )

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
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
    def test_create_failure_does_not_update_execution_context(
        self,
        settings,
        options_create,
        set_driver,
        set_browser,
        set_session_id,
    ):
        # Arrange
        settings.BROWSER = "chrome"
        settings.HEADLESS = False

        fake_options = Mock()

        options_create.return_value = fake_options

        failing_creator = Mock(
            side_effect=RuntimeError(
                "Browser failed to start"
            )
        )

        with patch.dict(
            DriverFactory._CREATORS,
            {
                Browser.CHROME: failing_creator,
            },
        ):
            # Act / Assert
            with pytest.raises(RuntimeError):
                DriverFactory.create()

        # Assert
        set_driver.assert_not_called()
        set_browser.assert_not_called()
        set_session_id.assert_not_called()

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_driver"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.driver"
    )
    def test_quit_clears_execution_context_even_when_driver_quit_fails(
        self,
        current_driver,
        set_driver,
        set_browser,
        set_session_id,
    ):
        # Arrange
        fake_driver = Mock()
        fake_driver.session_id = "session-123"

        fake_driver.quit.side_effect = RuntimeError(
            "Failed to close browser"
        )

        current_driver.return_value = fake_driver

        # Act / Assert
        with pytest.raises(RuntimeError):
            DriverFactory.quit()

        # Assert
        set_driver.assert_called_once_with(None)
        set_browser.assert_called_once_with(None)
        set_session_id.assert_called_once_with(None)

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
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
    def test_create_cleans_up_driver_when_execution_context_registration_fails(
        self,
        settings,
        options_create,
        set_driver,
        set_browser,
        set_session_id,
    ):
        # Arrange
        settings.BROWSER = "chrome"
        settings.HEADLESS = False

        fake_options = Mock()
        options_create.return_value = fake_options

        fake_driver = Mock()
        fake_driver.session_id = "session-123"

        fake_creator = Mock(
            return_value=fake_driver
        )

        # Simulate failure while registering browser metadata
        set_browser.side_effect = RuntimeError(
            "Failed to update execution context"
        )

        with patch.dict(
            DriverFactory._CREATORS,
            {
                Browser.CHROME: fake_creator,
            },
        ):
            # Act / Assert
            with pytest.raises(RuntimeError):
                DriverFactory.create()

        # The browser was created, so it must be cleaned up
        fake_driver.quit.assert_called_once()

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
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
    def test_create_clears_context_when_registration_and_cleanup_fail(
        self,
        settings,
        options_create,
        set_driver,
        set_browser,
        set_session_id,
    ):
        # Arrange
        settings.BROWSER = "chrome"
        settings.HEADLESS = False

        fake_options = Mock()
        options_create.return_value = fake_options

        fake_driver = Mock()
        fake_driver.session_id = "session-123"

        fake_driver.quit.side_effect = RuntimeError(
            "Browser cleanup failed"
        )

        fake_creator = Mock(
            return_value=fake_driver
        )

        # Simulate execution context registration failure
        set_browser.side_effect = RuntimeError(
            "Execution context registration failed"
        )

        with patch.dict(
            DriverFactory._CREATORS,
            {
                Browser.CHROME: fake_creator,
            },
        ):
            # Act / Assert
            with pytest.raises(RuntimeError):
                DriverFactory.create()

        # Browser cleanup was attempted
        fake_driver.quit.assert_called_once()

        # Execution context must still be cleared
        assert set_driver.call_args_list[-1].args == (None,)
        assert set_browser.call_args_list[-1].args == (None,)
        assert set_session_id.call_args_list[-1].args == (None,)

    @patch(
        "core.driver.driver_factory.ExecutionContext.set_session_id"
    )
    @patch(
        "core.driver.driver_factory.ExecutionContext.set_browser"
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
    def test_create_preserves_original_exception_when_cleanup_fails(
        self,
        settings,
        options_create,
        set_driver,
        set_browser,
        set_session_id,
    ):
        # Arrange

        settings.BROWSER = "chrome"
        settings.HEADLESS = False

        fake_options = Mock()
        options_create.return_value = fake_options

        fake_driver = Mock()
        fake_driver.session_id = "session-123"

        original_error = RuntimeError(
            "Execution context registration failed"
        )

        cleanup_error = RuntimeError(
            "Driver cleanup failed"
        )

        set_browser.side_effect = original_error
        fake_driver.quit.side_effect = cleanup_error

        fake_creator = Mock(
            return_value=fake_driver
        )

        with patch.dict(
            DriverFactory._CREATORS,
            {
                Browser.CHROME: fake_creator
            },
        ):

            # Act + Assert
            with pytest.raises(RuntimeError) as exc_info:
                DriverFactory.create()

        # The original error must be preserved
        assert exc_info.value is original_error