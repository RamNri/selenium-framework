from api.client.api_client import ApiClient
from api.responses.auth_response import AuthResponse

class AuthClient:
  def __init__(self, api_client: ApiClient):
    self._api_client = api_client

  def create_token(self, username, password):
    payload = {
      "username": username,
      "password": password
    }

    response = self._api_client.post("/auth", json=payload)
    return AuthResponse(response)

  def login(self, username, password):
    payload = {
      "username": username,
      "password": password
    }
    return self._api_client.post("/login", payload)