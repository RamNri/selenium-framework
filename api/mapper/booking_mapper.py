from api.models.booking import Booking
from api.models.booking_dates import BookingDates
from api.models.booking_request import BookingRequest

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
    
