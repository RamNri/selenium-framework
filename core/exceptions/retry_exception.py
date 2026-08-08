from core.exceptions.api_exceptions import ApiException

class RetryExhaustedException(ApiException):
  """
  Raised when retry policy exhauts all attempts.
  """
  pass
