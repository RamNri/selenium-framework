from api.auth.authentication_manager import AuthenticationManager
from api.clients.booking_client import BookingClient
from api.models.booking_request import BookingRequest
from api.responses.booking_response import BookingResponse

class BookingService:
  """
  Business service reponsible for booking operations.

  This layer orchestrates business workflows and hides
  authentication details from tests
  """

  def __init__(
      self, 
      booking_client: BookingClient,
      authentication_manager: AuthenticationManager
      ):
    
    self._client = booking_client
    self._authentication_manager = authentication_manager

  
  def create_booking(self, request: BookingRequest) -> BookingResponse:
    """
    Creates new booking
    """
    return self._client.create_booking(request)
  
  def get_booking(
      self,
      booking_id: int) -> BookingResponse:
    """
    Retrieves an existing booking
    """
    return self._client.get_booking(booking_id)
  
    
  def update_booking(
      self, 
      booking_id: int, 
      request: BookingRequest) -> BookingResponse:
    """updates an existing booking"""

    return self._client.update_booking(
      booking_id=booking_id, 
      equest=request,
      token=self._authentication_manager.get_token()
      )

  
  def delete_booking(
      self, 
      booking_id: int) -> BookingResponse:
    """Deletes an existing booking"""

    return self._client.delete_booking(
      booking_id=booking_id,
      token=self._authentication_manager.get_token()
      )
