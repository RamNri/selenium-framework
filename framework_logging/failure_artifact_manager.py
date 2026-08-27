from __future__ import annotations
import logging
from pathlib import Path
from datetime import datetime

from core.execution.execution_context import ExecutionContext
from pytest_html import extras
import base64

logger = logging.getLogger("framework.artifacts")

class FailureArtifactManager:
    """
    Responsible for creating and attaching artifacts produced
    when a test fails.

    Current responsibilities:
        - Capture browser screenshot
        - Attach screenshot to pytest-html report
    """
    @staticmethod
    def screenshot_path(test_name: str) -> Path:
        execution_id = ExecutionContext.execution_id()
        worker_id = ExecutionContext.worker_id()

        screenshot_dir = (
            Path("artifacts") / "screenshots" / str(worker_id) / str(execution_id)
        )

        screenshot_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = (f"{test_name}_{timestamp}.png")

        return screenshot_dir / filename

    @staticmethod
    def capture_screenshot(driver, test_name:str):
        """
        capture a screenshot from the current test execution.

        Returns:
          path to the screenshot if successful.
          None if screenshot capture fails
        """
        if driver is None:
            logger.warning("cannot capture screenshot because driver is None")
            return None

        filepath = FailureArtifactManager.screenshot_path(test_name)

        try:
            driver.save_screenshot(str(filepath))
            logger.info("screenshot captured: %s", filepath.resolve(),)
            return filepath
        except Exception:
            logger.exception("Failed to capture screenshot for test '%s'", test_name, )
            return None

    @staticmethod
    def attach_screenshot(report, filepath):
      """
      Attach a screenshot to the pytest-html report.
      """

      if filepath is None:
        return

      extra = getattr(report, "extras", [])

      with filepath.open("rb") as image_file:
        image_data = image_file.read()

      encoded_image = base64.b64encode(image_data).decode("utf-8")

      extra.append(
        extras.image(
            encoded_image,
            mime_type="image/png",
            extension="png",
        )
      )

      report.extras = extra