from api.clients.booking_client import BookingClient
from api.models.booking_request import BookingRequest
from api.responses.booking_response import BookingResponse

class BookingService:

  def __init__(self, booking_client: BookingClient):
    self._client = booking_client
  
  def create_booking(self, request: BookingRequest) -> BookingResponse:
    """
    Creates new booking
    """
    return self._client.create_booking(request)
    
  def update_booking(self, booking_id: int, request: BookingRequest) -> BookingResponse:
    """updates a booking"""

    return self._client.update_booking(booking_id, request)

  
  def delete_booking(self, booking_id: int) -> BookingResponse:
    """Deletes a booking"""

    return self._client.delete_booking(booking_id)
