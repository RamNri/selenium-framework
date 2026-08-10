from unittest.mock import Mock
import pytest
from api.auth.authentication_manager import AuthenticationManager
from core.exceptions import AuthenticationException

class TestAuthenticationManager:

  def test_failed_authentication_raises_exception(self):
    
    auth_reponse = Mock()
    auth_reponse.is_authenticated = False
    auth_reponse.error_message = "Bad credentials"

    auth_client = Mock()
    auth_client.create_token.return_value = auth_reponse

    manager = AuthenticationManager(
      auth_client,
      "admin",
      "wrong"
    )

    with pytest.raises(AuthenticationException):
      manager.get_token()
  
  def test_toaken_is_cached(self):
    auth_response = Mock()
    auth_response.is_authenticated = True
    auth_response.token = "abc123"
    auth_client = Mock()

    auth_client.create_token.return_value = auth_response
    manager = AuthenticationManager(
      auth_client,
      "admin",
      "password123"
    )

    token1 = manager.get_token()
    token2 = manager.get_token()

    assert  token1 == token2
    assert auth_client.create_token.call_count == 1