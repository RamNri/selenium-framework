from api.models.booking import Booking
from api.models.booking_dates import BookingDates
from api.models.booking_request import BookingRequest
from utilities.json_loader import JsonLoader
from config.paths import(DEFAULT_BOOKING, UPDATE_BOOKING, INVALID_BOOKING )
from core.data.fake_data import FakeData

class BookingBuilder:
 
  def __init__(self):
    self._firstname = None
    self._lastname = None
    self._totalprice = None
    self._depositpaid = None
    self._checkin = None
    self._checkout = None
    self._additionalneeds = None

  @classmethod
  def default(cls):
    return cls._from_json(DEFAULT_BOOKING)
  
  @classmethod
  def updated(cls):
    return cls._from_json(UPDATE_BOOKING)
  
  @classmethod
  def invalid(cls):
    return cls._from_json(INVALID_BOOKING)
  
  @classmethod
  def _from_json(cls, path):
    data = JsonLoader.load(path)
    builder = cls()

    builder._firstname = data["firstname"]
    builder._lastname = data["lastname"]
    builder._totalprice = data["totalprice"]  
    builder._depositpaid = data["depositpaid"]
    builder._checkin = data["bookingdates"]["checkin"]
    builder._checkout = data["bookingdates"]["checkout"]
    builder._additionalneeds = data["additionalneeds"]

    return builder  

  @classmethod
  def random(cls):
    builder = cls.default()

    checkin, checkout = FakeData.booking_dates()
    builder._firstname = FakeData.first_name()
    builder._lastname = FakeData.last_name()
    builder._totalprice = FakeData.total_price()
    builder._checkin = checkin
    builder._checkout= checkout

    builder._additionalneeds = (FakeData.additional_needs())
    return builder

  @classmethod
  def vip(cls):
    return (
      cls.random().with_totalprice(5000).with_additional_needs("Breakfast")
    )

  @classmethod
  def family_trip(cls):
    return (
      cls.random().with_additional_needs("Baby crib")
    )

  @classmethod
  def business_trip(cls):
    return(
      cls.random().with_additional_needs("Late Checkout")
    )
  
  def with_firstname(self, firstname: str):
    self._firstname = firstname
    return self
  
  def with_lastname(self, lastname: str):
    self._lastname = lastname
    return self
  
  def with_totalprice(self, totalprice: int):
    self._totalprice = totalprice
    return self
  
  def with_depositpaid(self, depositpaid: bool):
    self._depositpaid = depositpaid
    return self
  
  def with_checkin(self, checkin: str):
    self._checkin = checkin
    return self
  
  def with_checkout(self, checkout: str):
    self._checkout = checkout
    return self
  
  def with_additional_needs(self, needs: str):
    self._additionalneeds = needs
    return self
  
  def build(self):
    booking_dates = BookingDates(
       checkin = self._checkin,
       checkout = self._checkout
    )

    booking = Booking(
      firstname=self._firstname,
      lastname=self._lastname,
      totalprice=self._totalprice,
      depositpaid=self._depositpaid,
      bookingdates=booking_dates,
      additionalneeds=self._additionalneeds)
    
    return BookingRequest(booking)