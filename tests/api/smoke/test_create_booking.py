import pytest
from api.builders.booking_builder import BookingBuilder
from api.factories.api_factory import ApiFactory

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
  assert response.ok

  assert response.is_create_response

  assert response.booking_id is not None

  assert response.booking is not None

  assert(response.booking.firstname == request.booking.firstname)

  assert(response.booking.lastname == request.booking.lastname)

  assert(response.booking.totalprice == request.booking.totalprice)

  assert(response.booking.depositpaid == request.booking.depositpaid)