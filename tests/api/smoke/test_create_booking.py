import pytest
from api.builders.booking_builder import BookingBuilder
from assertions.api.booking_assertion import BookingAssertions
from services.BookingService import BookingService

@pytest.mark.smoke
@pytest.mark.api
def test_create_booking(booking_service: BookingService):

  #Arrange
  request = (BookingBuilder.default().with_firstname("Guru").with_lastname("ji").build())

  #Act
  response = booking_service.create_booking(request)

  #Assert
  BookingAssertions.assert_create_booking(request, response)
