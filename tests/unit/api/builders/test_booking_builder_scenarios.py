from api.builders.booking_builder import BookingBuilder

class TestBookingBuilderScenarios:

  def test_vip_booking(self):

    booking = BookingBuilder.vip().build().booking
    assert booking.totalprice == 5000
    assert booking.additionalneeds == "Breakfast"

  def test_family_trip(self):
    booking = BookingBuilder.family_trip().build().booking
    assert booking.additionalneeds == "Baby crib"

  def test_business_trip(self):
    booking = BookingBuilder.business_trip().build().booking
    assert booking.additionalneeds == "Late Checkout"
