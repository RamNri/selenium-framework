import pytest
from api.builders.booking_builder import BookingBuilder
from api.factories.api_factory import ApiFactory
from assertions.api.booking_assertion import BookingAssertions

@pytest.fixture(scope="module")
def booking_service():
  """
  REturns Bookingservice.
  """
  return ApiFactory().get_booking_service()

def test_create_booking_successfully(booking_service):
  """
  Verify a booking can be created successfully
  """
  #Arrange
  request = BookingBuilder.default().build()

  #Act
  response = booking_service.create_booking(request)

  #Assert
  BookingAssertions.assert_booking_equals(request.booking, response.booking)