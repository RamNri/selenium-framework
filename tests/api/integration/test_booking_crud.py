import pytest

from api.builders.booking_builder import BookingBuilder
from api.factories.api_factory import ApiFactory

from assertions.api.booking_assertion import BookingAssertions
from assertions.api.api_assertion import ApiAssertions

@pytest.fixture(scope="module")
def booking_service():
  """
  Returns BookingService
  """
  return ApiFactory().get_booking_service()

def test_booking_crud_workflow(booking_service):
  """
  To verify complete Booking CRUD wrokflow.

  Create -> Get -> Update -> Get -> Delete
  """

  #Arrange
  create_request = BookingBuilder.default().build()
  update_request = BookingBuilder.updated().build()

  #Create
  create_response = booking_service.create_booking(create_request)

  #Assert
  BookingAssertions.assert_create_booking(create_request, create_response)

  booking_id = create_response.booking_id

  #GET

  get_response = booking_service.get_booking(booking_id)

  BookingAssertions.assert_get_booking(create_request, get_response)

  #UPDATE
  update_response = booking_service.update_booking(booking_id, update_request)

  #Assert
  BookingAssertions.assert_update_booking(update_request, update_response)

  #Get updated booking
  get_updated_response = booking_service.get_booking(booking_id)

  #Assert
  BookingAssertions.assert_get_booking(update_request, get_updated_response)

  #DELETE

  delete_response = booking_service.delete_booking(booking_id)

  BookingAssertions.assert_delete_booking(delete_response)

  get_deleted_response = booking_service.get_booking(booking_id)

  BookingAssertions.assert_booking_not_found(get_deleted_response)