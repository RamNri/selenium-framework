from api.models.booking import Booking
from api.models.booking_dates import BookingDates
from api.models.booking_request import BookingRequest
from core.exceptions import MappingException
import logging

logger = logging.getLogger(__name__)

class BookingMapper:

  @staticmethod
  def to_request(request: BookingRequest) -> dict:
    booking = request.booking
    return {
      "firstname": booking.firstname,
      "lastname": booking.lastname,
      "totalprice": booking.totalprice,
      "depositpaid": booking.depositpaid,
      "bookingdates": {
        "checkin" : booking.bookingdates.checkin,
        "checkout": booking.bookingdates.checkout
      },
      "additionalneeds": booking.additionalneeds
    }
  
  @staticmethod
  def from_response(data: dict) -> Booking:
    """
        Maps API response JSON into a strongly typed Booking model.
    """
    try:

      if "booking" in data:
        data = data["booking"]

      booking_dates = BookingDates(

        checkin=data["bookingdates"]["checkin"],
        checkout=data["bookingdates"]["checkout"]
        )
    
      return Booking(
        firstname=data["firstname"],
        lastname=data["lastname"],
        totalprice=data["totalprice"],
        depositpaid=data["depositpaid"],
        bookingdates=booking_dates,
        additionalneeds=data.get("additionalneeds")
      )
    except KeyError as ex:
      logger.error( "Booking mapping failed. Missing field '%s'.", ex.args[0])
      raise MappingException(
        f"Missing Required field '{ex.args[0]}' while mapping Booknig Response"
      ) from ex
    
    except TypeError as ex:
      logger.error("Booking mapping has invalid structure.")
      raise MappingException(
        "Invalid Booking response structure received from API."
      ) from ex
    
