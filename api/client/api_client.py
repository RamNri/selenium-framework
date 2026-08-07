import requests
from config import settings
from framework_logging.api_logger import ApiLogger

class ApiClient:
  def __init__(self, session: requests.Session, base_url: str, timeout: int=30):
    self._base_url = base_url.rstrip("/")
    self._session = session
    self._timeout = timeout
  
  def request(self, method: str, endpoint: str, **kwargs):
    endpoint = endpoint.lstrip("/")
    url = f"{self._base_url}/{endpoint}"

    ApiLogger.log_request(method=method, url=url, headers=kwargs.get("headers"), body=kwargs.get("json"))
    response = self._session.request(
      method=method,
      url=url, 
      timeout=self._timeout, 
      **kwargs)
    
    ApiLogger.log_response(response)

    return response

  def get(self, endpoint, **kwargs):
    return self.request("GET", endpoint, **kwargs)
  
  def post(self, endpoint, **kwargs):
    return self.request("POST", endpoint, **kwargs)
  
  def put(self, endpoint, **kwargs):
    return self.request("PUT", endpoint, **kwargs)
  
  def delete(self, endpoint, **kwargs):
    return self.request("DELETE", endpoint, **kwargs)
