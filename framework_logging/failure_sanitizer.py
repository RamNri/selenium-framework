from __future__ import annotations
import re

class FailureSanitizer:
  """
  Sanitizes pytest failure representations before they are logged.

  The goal is to prevent sensitive values such as passwords, token, API Keys
  and secrets from appearing in framework logs
  """
  SENSITIVE_PATTERN = (
    r"(password\s*=\s*)(['\"])(.*?)(\2)",
    r"(token\s*=\s*)(['\"])(.*?)(\2)",
    r"(api[_-]?key\s*=\s*)(['\"])(.*?)(\2)",
    r"(secrets\s*=\s*)(['\"])(.*?)(\2)"
  )

  MASK= r"\1\2********\4"

  @classmethod
  def sanitize(cls, failure_text: str) -> str:
    """
    Return a sanitized copy of pytest failure text.
    The original failure text is never modified
    """

    if not failure_text:
      return failure_text

    sanitized = failure_text

    for pattern in cls.SENSITIVE_PATTERN:
      sanitized = re.sub(pattern, cls.MASK, sanitized, flags=re.IGNORECASE)

    return sanitized