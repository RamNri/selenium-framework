from api.client.api_client import ApiClient
from api.responses.booking_response import BookingResponse
from api.mapper.booking_mapper import BookingMapper
from api.models.booking_request import BookingRequest

class BookingClient:
  """
  Client responsible for communicating with the Booking endpoints
  """

  def __init__(self, api_client: ApiClient):
    self._client = api_client

  
  def create_booking(self, request: BookingRequest) -> BookingResponse:
    """
    Creates a new booking,

    Args: 
      request: BookingRequest 
    
    Returns:
      BookingResponse
    """
    payload = BookingMapper.to_request(request)
    response = self._client.post("/booking", json=payload)
    return BookingResponse(response)
  
  def get_booking(self, booking_id: int) -> BookingResponse:
    response = self._client.get(f"/booking/{booking_id}")
    return BookingResponse(response)
  
  def update_booking(
      self, 
      booking_id: int, 
      request: BookingRequest,
      token:str) -> BookingResponse:
    
    """ updates an existing booking """

    payload = BookingMapper.to_request(request)
    headers = {
      "Cookie" : f"token={token}"
    }
    response  = self._client.put(f"/booking/{booking_id}", json=payload, headers=headers)
    return BookingResponse(response)
  
  def delete_booking(
      self, 
      booking_id: int, 
      token: str) -> BookingResponse:
    """Deletes a booking"""

    headers = {
      "Cookie": f"token={token}"
    }
    response = self._client.delete(f"/booking/{booking_id}", headers=headers)
    return BookingResponse(response)

# TODO:
# Add request/response logging.
# Add retry support.
# Add request timing metrics.
# Add request correlation id.