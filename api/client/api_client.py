import requests
from config import settings

class ApiClient:
  def __init__(self, session: requests.Session, base_url: str, timeout: int=30):
    self._base_url = base_url.rstrip("/")
    self._session = session
    self._timeout = timeout
  
  def request(self, method, endpoint, **kwargs):
    endpoint = endpoint.lstrip("/")
    return self._session.request(method=method, url=f"{self._base_url}/{endpoint}", 
                                timeout=self._timeout, 
                                **kwargs)

  def get(self, endpoint, **kwargs):
    return self.request("GET", endpoint, **kwargs)
  
  def post(self, endpoint, **kwargs):
    return self.request("POST", endpoint, **kwargs)
  
  def put(self, endpoint, **kwargs):
    return self.request("PUT", endpoint, **kwargs)
  
  def delete(self, endpoint, **kwargs):
    return self.request("DELETE", endpoint, **kwargs)
