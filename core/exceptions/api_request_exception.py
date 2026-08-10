from core.exceptions import ApiException

class ApiRequestException(ApiException):
  """
  Raised when an HTTP request cannot be completed
  """
  pass