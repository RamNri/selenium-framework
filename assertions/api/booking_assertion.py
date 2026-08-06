from assertions.api.api_assertion import ApiAssertions

from api.models.booking import Booking
from api.responses.booking_response import BookingResponse
from api.models.booking_request import BookingRequest

from config import settings

class BookingAssertions:

  """
  Assertion helpers for Booking API.
  Keeps test method samll, readable adn reusable
  """
  
  @staticmethod
  def assert_create_booking(
     request: BookingRequest, 
     response: BookingResponse
     ) -> None:
    
    """
    Verify create booking response.
    """


    ApiAssertions.assert_status(response, 200)
    ApiAssertions.assert_response_time(response, settings.MAX_API_RESPONSE_TIME)

    assert response.booking_id is not None,(
      "Booking id should not be none"
    )
    assert response.booking is not None, (
      "Booking object should not be no"
    )

    BookingAssertions.assert_booking_equals(request.booking, response.booking)

  @staticmethod
  def assert_get_booking(
     expected_request: BookingRequest, 
     response: BookingResponse
     ) -> None:

     """
     Verify Get Booking response
     """

     ApiAssertions.assert_status(response, 200)
     ApiAssertions.assert_response_time(response, settings.MAX_API_RESPONSE_TIME)

     assert response.booking is not None, (
        "Booking object should not be None."
        )

     BookingAssertions.assert_booking_equals(expected_request.booking, response.booking)

  @staticmethod
  def assert_booking_equals(
     expected: Booking,
     actual: Booking
     ) -> None:
      
      """
      Compare two Booking objects field-by-field
      """
      assert expected == actual, (
         "\nBooking objects do not match.\n\n"
         f"Expected:\n{expected}\n\n"
         f"Actual:\n{actual}" 
      )
  
  @staticmethod
  def assert_update_booking(
     request: BookingRequest,
     response: BookingResponse
  ) -> None:
     
     """
     Verify update Booking response.
     """

     ApiAssertions.assert_status(response, 200)
     ApiAssertions.assert_response_time(response, settings.MAX_API_RESPONSE_TIME)

     assert response.booking is not None, ("Updated booking should not be None.")

     BookingAssertions.assert_booking_equals(request.booking, response.booking)

  @staticmethod
  def assert_delete_booking(response: BookingResponse) -> None:
     """
     Verfiy Delete Booking response
     """

     ApiAssertions.assert_status(response, 201)
     ApiAssertions.assert_response_time(response, settings.MAX_API_RESPONSE_TIME)