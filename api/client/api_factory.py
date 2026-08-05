from api.auth.authentication_manager import AuthenticationManager
from api.client.api_client import ApiClient
from api.clients.auth_client import AuthClient
from api.client.booking_client import BookingClient

class ApiFactor:

  def __init__(self):
    auth_manager = AuthenticationManager()
    session = auth_manager.get_session()
    self._api_client = ApiClient(session)

    self._auth_client=None
    self._booking_client=None

  def get_auth_client(self):
    if self._auth_client is None:
      self._auth_client = AuthClient(self._api_client)
    return self._auth_client
  
  def get_booking_client(self):
    if self._booking_client is None:
      self._booking_client = BookingClient(self._api_client)
    return self._booking_client