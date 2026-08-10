from core.exceptions.api_exception import ApiException

class RetryExhaustedException(ApiException):
  """
  Raised when retry policy exhauts all attempts.
  """
  pass
