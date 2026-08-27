from unittest.mock import Mock

from framework_logging.failure_artifact_manager import FailureArtifactManager

class TestFailureArtifactManager:

  def test_screenshot_path_contains_worker_and_execution_id(
      self, monkeypatch, tmp_path,):

    monkeypatch.chdir(tmp_path)
    path = FailureArtifactManager.screenshot_path("test_login")

    assert "artifacts" in path.parts
    assert "screenshots" in path.parts
    assert path.parent.exists()
    assert path.name.startswith("test_login")
    assert path.suffix == ".png"

  def test_capture_screenshot_calls_driver(self, monkeypatch, tmp_path,):
    monkeypatch.chdir(tmp_path)
    driver = Mock()
    path = FailureArtifactManager.capture_screenshot(driver, "test_login",)
    driver.save_screenshot.assert_called_once_with(str(path))
    assert path is not None

  def test_capture_screenshot_returns_none_when_driver_is_none(self):
    result = FailureArtifactManager.capture_screenshot(None, "test_login",)
    assert result is None

  def test_capture_screenshot_does_not_crash_when_driver_fails(self, monkeypatch, tmp_path,) :
    monkeypatch.chdir(tmp_path)
    driver = Mock()
    driver.save_screenshot.side_effect = Exception("Browser crashed")
    result = FailureArtifactManager.capture_screenshot(driver, "test_login",)
    assert result is None

  def test_attach_screenshot_adds_image_to_report(self, tmp_path,):
    report = Mock()
    report.extras = []
    screenshot = tmp_path / "failure.png"
    screenshot.write_bytes(b"fake image")
    FailureArtifactManager.attach_screenshot(report, screenshot,)
    assert len(report.extras) == 1

  def test_attach_screenshot_does_nothing_for_none(self):
    report = Mock()
    report.extras = []
    FailureArtifactManager.attach_screenshot(report, None,)
    assert report.extras == []
