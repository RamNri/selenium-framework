from dataclasses import dataclass
from api.models.booking_dates import BookingDates

@dataclass(slots=True, frozen=True)
class Booking:
  """
  Represents a booking domian object
  """
 
  firstname: str
  lastname: str
  totalprice: str
  depositpaid: str
  bookingdates: BookingDates
  additionalneeds: str
