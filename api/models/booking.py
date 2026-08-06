from api.models.booking_dates import BookingDates

class Booking:
  def __init__(
    self,
    firstname: str,
    lastname: str,
    totalprice: int,
    depositpaid: bool,
    bookingdates: BookingDates,
   additionalneeds: str = None
   ):
    
    self.firstname =firstname
    self.lastname = lastname
    self.totalprice = totalprice
    self.depositpaid = depositpaid
    self.bookingdates = bookingdates
    self.additionalneeds = additionalneeds
 
  def __repr__(self):
    return (
      f"Booking("
      f"firstname='{self.firstname}',"
      f"lastname='{self.lastname}',"
      f"totalprice='{self.totalprice}',"
      f"depositpaid='{self.depositpaid}',"
      f"bookingdates='{self.bookingdates}',"
      f"additionalneeds='{self.additionalneeds}',"
      ")"
    )
  
  def __eq__(self, other):
    """
    Compare two Booking objects.
    """

    if not isinstance(other, Booking):
      return NotImplemented
    
    return(
      self.firstname == other.firstname
      and self.lastname == other.lastname
      and self.totalprice == other.totalprice
      and self.depositpaid == other.depositpaid
      and self.bookingdates == other.BookingDates
      and self.additionalneeds == others.additionalneeds
    )

