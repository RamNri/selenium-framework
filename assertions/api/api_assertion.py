from api.responses.base_response import BaseResponse

class ApiAssertions:

  @staticmethod
  def assert_status(response: BaseResponse, expected_status: int):
    assert response.status_code == expected_status
  
  @staticmethod
  def assert_response_time(response: BaseResponse, max_seconds: float):
    assert (response.elapsed.total_seconds() <= max_seconds)
