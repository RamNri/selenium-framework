import json

class LogUtils:

  SENSITIVE_FIELDS = {
    "password",
    "token",
    "access_token",
    "refresh_token",
    "authorization",
    "api_key",
    "secret",
    "client_secret",
  }

  SENSITIVE_HEADERS = {
    "authorization",
    "cookie",
    "token"
  }

  @staticmethod
  def pretty_json(data):
    return json.dumps(
    data,
    indent=4,
    default=str
  )


  @staticmethod
  def mask_headers( headers: dict | None,) -> dict:
    if not headers:
      return {}
  
    masked = {}

    for key, value in headers.items():
      if key.lower() in LogUtils.SENSITIVE_HEADERS:
        masked[key] = "********"
      else:
        masked[key] = value
    return masked

  @staticmethod
  def mask_sensitive_data(data):
    if isinstance(data, dict):
      return {
        key: (
          "********"
          if key.lower() in LogUtils.SENSITIVE_FIELDS
          else LogUtils.mask_sensitive_data(value)
        )
        for key, value in data.items()
      }

    if isinstance(data, list):
      return[
        LogUtils.mask_sensitive_data(item)
        for item in data
      ]

    return data