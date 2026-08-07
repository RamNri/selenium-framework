import json

class LogUtils:

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
