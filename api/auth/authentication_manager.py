from __future__ import annotations
from threading import Lock
from api.clients.auth_client import AuthClient
from core.exceptions.authentication_exception import (AuthenticationException,)
import logging

logger = logging.getLogger(__name__)

class AuthenticationManager:
  """
  Responsible for managing authentication tokens.

  Responsibilities:
    - Authenticate using AuthClient.
    - Cache authentication token.
    - Return cached token whenever possible.
    - Be thred-safe for future parallel execution
  """

  def __init__(self, auth_client: AuthClient, username: str, password: str ):
    self._auth_client = auth_client
    self._username = username
    self._password = password
    self._token: str | None = None
    self._lock = Lock()

  def get_token(self):
    """
    Returns a valid authentication token.
    Authentication happens only once.
    Subsequent calls resuse the cached token.

    Returns:
        str: Authentication token.
    """
    #(alredy authenticated)
    if self._token is not None:
      return self._token

    #Thread safe authentication
    with self._lock:
       
       #Another thread may already have authenticated
      if self._token is not None:
         return self._token
 
      auth_response = self._auth_client.create_token(
        self._username,
        self._password
      )

      if not auth_response.is_authenticated:
        logger.error(
          "Authentication failed for user '%s'. Reason: %s",self._username, auth_response.error_message
        )
        raise AuthenticationException(
          f"Authentication failed for the user"
          f"'{self._username}'."
          f"Reason:{auth_response.error_message}"
        )
      
      self._token = auth_response.token

      logger.info("Authentication successful for user '%s'.", self._username)

      return self._token
  
  def invalidate(self) -> None:
    """
    Clears the cached authentication token.
    The next call to get_token() will authenticate again.
    """
    with self._lock:
      self._token = None