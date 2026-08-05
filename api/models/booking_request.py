from api.models.booking import Booking

class BookingRequest:
  
  def __init__(self, booking: Booking):
    self.booking = booking
