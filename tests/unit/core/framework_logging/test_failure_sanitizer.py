from framework_logging.failure_sanitizer import FailureSanitizer

class TestFailureSanitizer:

  def test_masks_passwrod(self):
    failure = (
      "username = 'standard_user'\n"
      "password = 'secret_sauce'"
    )

    result = FailureSanitizer.sanitize(failure)
    assert "secret_sauce" not in result
    assert "password = '********'" in result

  def test_masks_token(self):
    failure = "token = 'abc123xyz'"
    result = FailureSanitizer.sanitize(failure)

    assert "abc123xyz" not in result
    assert "token = '********'" in result

  def test_masks_api_key(self):
    failure = "api_key = 'my-secret-key'"
    result = FailureSanitizer.sanitize(failure)

    assert "my-secret-key" not in result
    assert "api_key = '********'" in result

  def test_non_sensitive_data_is_preserved(self):
    failure = (
      "username = 'standard_user'\n"
      "status = 200\n"
      "AssertionError"
    )

    result = FailureSanitizer.sanitize(failure)
    assert result == failure

  def test_original_text_is_not_modified(self):
    failure = "password = 'secret_sauce'"
    FailureSanitizer.sanitize(failure)
    assert failure == "password = 'secret_sauce'"