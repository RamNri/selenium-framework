from api.responses.base_response import BaseResponse

class AuthResponse(BaseResponse):

  def __init__(self, response):
    super().__init__(response)
  
  @property
  def token(self):
    return self.body.get("token")
  
  @property
  def is_authenticated(self):
    return self.ok and self.token is not None

  @property
  def authentication_failed(self):
    return not self.is_authenticated  
  
  @property
  def error_message(self):
    return (
      self.body.get("reaons")
      or self.body.get("message")
      or ""
    )

  @property
  def reason(self):
    return self.body.get("reason")