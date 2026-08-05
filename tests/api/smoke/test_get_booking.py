import pytest
from api.builders.booking_builder import BookingBuilder
from assertions.api.booking_assertion import BookingAssertions
from services.BookingService import BookingService

@pytest.test.smoke
@pytest.test.api
def test_get_booking(booking_service: BookingService):
  # Arrange
  request = (BookingBuilder.default().with_firstname("Guru").with_lastname("ji").build())

  #Create booking
  create_response = booking_service.create_booking(request)
  BookingAssertions.assert_create_booking(request, create_response)

  booking_id = create_response.booking_id

  #Get booking
  get_response = booking_service.get_booking( booking_id)

  # Assert

  BookingAssertions.assert_get_booking( request, get_response)
