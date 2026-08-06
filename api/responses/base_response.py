from requests.exceptions import JSONDecodeError

class BaseResponse:
  def __init__(self, response):
    self.response = response
    self.body = self._parse_json()

  def _parse_json(self):
    try:
      return self.response.json()
    except ValueError:
      return {}
   
  @property
  def status_code(self):
    return self.response.status_code
  
  @property
  def headers(self):
    return self.response.headers
  
  @property
  def text(self):
    return self.response.text
  
  @property
  def elapsed(self):
    return self.response.elapsed
  
  @property
  def ok(self):
    return self.response.ok
  
  @property
  def is_json(self):
    return bool(self.body)
  
  @property
  def json(self):
    try:
      return self.response.json()
    except JSONDecodeError:
      return None
  
  