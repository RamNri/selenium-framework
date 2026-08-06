import pytest
from api.builders.booking_builder import BookingBuilder
from api.factories.api_factory import ApiFactory
from assertions.api.booking_assertion import BookingAssertions

@pytest.fixture(scope="module")
def booking_service():
  return ApiFactory().get_booking_service()


def test_get_booking_successfully(booking_service):
  """
  Verify a booking can be retrieved successfully.
  """

  # Arrange
  request = BookingBuilder.default().build()
  
  #Create booking
  create_response = booking_service.create_booking(request)
  
  BookingAssertions.assert_create_booking(request, create_response)

  booking_id = create_response.booking_id

  #Get booking
  get_response = booking_service.get_booking(booking_id)

  # Assert

  BookingAssertions.assert_get_booking( request, get_response)
