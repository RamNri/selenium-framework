class BookingDates:
  """
  Represents the booking check-in and check-out dates
  """
  def __init__(
    self, 
    checkin: str,
    checkout: str
  ):
    self.checkin = checkin
    self.checkout = checkout
  
  def __repr__(self):
    return(
      "BooknigDates("
      f"checkin='{self.checkin}'."
      f"checkout='{self.checkout}',"
    )
  
  def __eq__(self, other):
    """
    compare two BookingDates objects
    """

    if not isinstance(other, BookingDates):
      return NotImplemented
    
    return(
      self.checkin == other.checkin
      and self.checkout == other.checkout
    )
  