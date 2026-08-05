from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class BookingDates:
  """
  Represents the booking check-in and check-out dates
  """
  
  checkin: str
  checkout: str