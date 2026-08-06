from api.mapper.booking_mapper import BookingMapper
from api.responses.base_response import BaseResponse

class BookingResponse(BaseResponse):
  """
  Wrapper around booking API responses.
  Responsible for expoisng strongly typed models instead of raw json
  """  
  def __init__(self, response):
    super().__init__(response)
    self.booking = None
    self.booking_id = None

    if not self.ok:
      return
    
    data = self.json

    if not isinstance(data, dict):
      return
    
    #Post /booking api
    
    if self.is_create_response:
      self.booking_id = data.get("bookingid")

      self.booking = BookingMapper.from_response(data)

      return
    
    #Get /booking/{id}
    self.booking = BookingMapper.from_response(data)
   
  
  @property
  def is_create_response(self):
    return (
      isinstance(self.json, dict)
      and "booking" in self.json
      and "bookingid" in self.json
    )