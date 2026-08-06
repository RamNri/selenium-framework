import requests
from config import settings
from api.auth.authentication_manager import AuthenticationManager
from api.client.api_client import ApiClient
from api.clients.auth_client import AuthClient
from api.clients.booking_client import BookingClient
from services.booking_service import BookingService

class ApiFactory:
  """
  Responsible for constructing and wiring all API dependencies.
  This class acts as the Dependency injection container for the API framework
  """

  def __init__(self):

    # Authentication session

    auth_session = requests.Session()
    auth_api_client = ApiClient(
      session=auth_session,
      base_url=settings.API_BASE_URL,
      timeout=settings.REQUEST_TIMEOUT
    )

    auth_client = AuthClient(auth_api_client)

    self._authentication_manager = AuthenticationManager(
      auth_client=auth_client,
      username=settings.API_USERNAME,
      password=settings.API_PASSWORD
    )

    #Authenitcated Session

    api_session = requests.Session()

    api_client=ApiClient(
      session=api_session,
      base_url=settings.API_BASE_URL,
      timeout=settings.REQUEST_TIMEOUT

    )

    booking_client = BookingClient(api_client)

    #Services
    self._booking_service = BookingService(
      booking_client=booking_client,
      authentication_manager=self._authentication_manager
    )

  def get_booking_service(self) -> BookingService:
    """
    Returns BookingService singleton.
    """
    return self._booking_service