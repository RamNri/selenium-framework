from api.models.booking import Booking
from api.responses.base_response import BaseResponse

class BookingResponse(BaseResponse):
  
  def __init__(self, response):
    super().__init__(response)
    self.booking = None
    self.booking_id = None

    if not self.ok:
      return
    
    data = self.json

    if not isinstance(data, dict):
      return
    
    if self.is_create_response:
      self.booking_id = data.get("bookingid")

      self.booking = Booking(data.get("booking", {}))
    else:

      self.booking= Booking(data)
  
  @property
  def is_create_response(self):
    return (
      isinstance(self.json, dict)
      and "booking" in self.json
    )

  @property
  def is_booking_found(self):
    return self.ok and self.booking is not None