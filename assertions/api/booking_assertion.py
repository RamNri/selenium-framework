from assertions.api.api_assertion import ApiAssertions
from api.models.booking import Booking
from api.responses.booking_response import BookingResponse
from api.models.booking_request import BookingRequest

class BookingAssertions:
  
  @staticmethod
  def assert_create_booking(request: BookingRequest, response: BookingResponse):
    
    ApiAssertions.assert_status(response, 200)
    ApiAssertions.assert_response_time(response, 5)

    assert response.booking_id is not None,(
      "Booking id should not be none"
    )
    assert response.booking is not None, (
      "Booking object should not be no"
    )

    BookingAssertions.assert_booking_equals(request.booking, response.booking)

  @staticmethod
  def assert_get_booking(expected_request: BookingRequest, response: BookingResponse):
     ApiAssertions.assert_status(response, 200)
     ApiAssertions.assert_response_time(response, 5)

     assert response.booking is not None, ("Booking object should not be None.")

     BookingAssertions.assert_booking_equals(expected_request.booking, response.booking)

  @staticmethod
  def assert_booking_equals(expected: Booking, actual: Booking):
      assert expected == actual