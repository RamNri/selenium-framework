from dataclasses import dataclass
from api.models.booking import Booking

@dataclass(slots=True, frozen=True)
class BookingRequest:
  
  """
  Request model used to create or update bookings
  """
  booking: Booking