from api.client.api_client import ApiClient
from api.responses.booking_response import BookingResponse
from api.mapper.booking_mapper import BookingMapper
from api.models.booking_request import BookingRequest
from api.responses.base_response import BaseResponse

class BookingClient:
  """
  Client responsible for communicating with the Booking endpoints
  """

  def __init__(self, api_client: ApiClient):
    self.__client = api_client

  
  def create_booking(self, request: BookingRequest) -> BookingResponse:
    """
    Creates a new booking,

    Args: 
      request: BookingRequest 
    
    Returns:
      BookingResponse
    """
    payload = BookingMapper.to_request(request)
    response = self.__client.post("/booking", json=payload)
    return BookingResponse(response)
  
  def get_booking(self, booking_id: int) -> BookingResponse:
    """
    Retrieves a  booking
    """
    response = self.__client.get(f"/booking/{booking_id}")
    return BookingResponse(response)
  
  def update_booking(
      self, 
      booking_id: int, 
      request: BookingRequest,
      token: str) -> BookingResponse:
    
    """ updates an existing booking """

    payload = BookingMapper.to_request(request)
    headers = {"Cookie" : f"token={token}"}
    response  = self.__client.put(f"/booking/{booking_id}", json=payload, headers=headers)
    return BookingResponse(response)
  
  def delete_booking(
      self, 
      booking_id: int, 
      token: str) -> BookingResponse:
    """Deletes a booking"""

    headers = {
      "Cookie": f"token={token}"
    }
    response = self.__client.delete(f"/booking/{booking_id}", headers=headers)
    return BaseResponse(response)

# TODO:
# Add request/response logging.
# Add retry support.
# Add request timing metrics.
# Add request correlation id.