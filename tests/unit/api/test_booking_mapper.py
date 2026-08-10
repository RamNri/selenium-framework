import pytest
from api.mapper.booking_mapper import BookingMapper
from core.exceptions import MappingException

class TestBookingMapper:

  def test_missing_requerired_field_raises_mapping_exception(self):

    response ={
     "booking": {
       "lastname" : "Smith"
     }
    }

    with pytest.raises(MappingException):
      BookingMapper.from_response(response)
    
  def test_invalid_bookingdates_structure_raises_mapping_exception(self):

    response = {
      "booking" : {
        "firstname" : "John",
        "lastname" : "Smith",
        "totalprice" : 100,
        "depositpaid" : True,
        "bookingdates" : None,
      }
    }

    with pytest.raises(MappingException):
      BookingMapper.from_response(response)