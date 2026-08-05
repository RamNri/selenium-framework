import requests
from api.clients.auth_client import AuthClient
from config import settings

class AuthenticationManager:

  def __init_(self, auth_client: AuthClient, username: str, password: str ):
    self._auth_client = auth_client
    self._username = username
    self._password = password
    self._token = None
    self._session = None

  def get_token(self):
    """
    Authenticate only once and cache the token

    """
    if self._token is None:

      auth = self._auth_client.create_token(
        self._username,
        self._password
      )

      if not auth.is_authenticated:
        raise RuntimeError(
          f"Authentication failed"
          f"{auth.error_message}"
        )
      
      self._token = auth.token

    return self._token
  
  def get_session(self):
    """
    Return one authenticated request.Session()

    """

    if self._session is None:
      session = requests.Session()
      session.headers.update(
        {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cookie": f"token{self.get_token()}"

      })
      self._session = session
    return self._session
