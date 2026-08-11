from api.builders.booking_builder import BookingBuilder

class TestBookingBuilder:

  def test_random_booking(self):

    request = (BookingBuilder.random().build())

    booking = request.booking

    assert booking.firstname
    assert booking.lastname

    assert booking.totalprice >= 100

    assert(booking.additionalneeds is not None)

    assert(booking.bookingdates.checkout > booking.bookingdates.checkin)
