import pytest

@pytest.mark.artifact_validation
def test_failure_artifact(driver):
  driver.get("https://www.saucedemo.com")
  assert False, "Intentional failure to verify failure artifact pipline"