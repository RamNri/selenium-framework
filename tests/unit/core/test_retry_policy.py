
import requests
from unittest.mock import Mock, call
from core.retry_policy import RetryPolicy
from core.exceptions import RetryExhaustedException

class TestRetryPolicy:
  """
  Unit tests for RetryPolicy
  """
  
  def setup_method(self):
    self.fake_sleep = Mock()
    self.policy = RetryPolicy(retries=3, delay=1, backoff=2, retry_status_codes={500, 502, 503, 504,}, sleeper=self.fake_sleep)

  def test_returns_response_without_retry(self):
    """
    Successful request test
    status code journey : 200
    """
   #Arrange
    response = Mock()
    response.status_code = 200
    operation = Mock(return_value=response)
    
    #Act
    result = self.policy.execute(operation)

    #Assert
    assert result == response
    assert operation.call_count == 1

  def test_retries_retryable_status_codes(self):
    """
    Retryable status 
    status code journey: 503 -> 503 -> 200
    """
    #Arrange
    response1 = Mock()
    response1.status_code = 503

    response2 = Mock()
    response2.status_code = 503

    response3 = Mock()
    response3.status_code = 200

    #Mock
    operation = Mock(side_effect=[response1, response2, response3])
    #Everytime RetryPolicy calls operation() it gets the next response

    result = self.policy.execute(operation)
    assert result.status_code == 200
    assert operation.call_count == 3

    self.fake_sleep.assert_has_calls(
      [
        call(1),
        call(2),
      ]
    )

  def test_does_not_retry_non_retryable_status(self):
      """
      Retryable status 
      status code journey: 404
      """
      response = Mock()
      response.status_code = 404
      operation = Mock(return_value=response)
      result = self.policy.execute(operation)
  
      assert result.status_code == 404
      assert operation.call_count == 1
      self.fake_sleep.assert_not_called()
  

  def test_retries_timeout_exception_then_succeeds(self):

      response = Mock()
      response.status_code = 200
    
      operation = Mock(
        side_effect=[
          requests.Timeout(),
          requests.Timeout(),
          response,
        ])
    
      result = self.policy.execute(operation)

      assert result.status_code == 200
      assert operation.call_count == 3
      self.fake_sleep.assert_has_calls(
       [
        call(1),
        call(2),
       ]
    )

  def test_raises_timeout_after_max_retries(self):
      operation = Mock(side_effect=requests.Timeout())

      import pytest
      with pytest.raises(RetryExhaustedException) as ex:
        self.policy.execute(operation)
      
      assert isinstance(ex.value.__cause__, requests.Timeout)
    
      assert operation.call_count == 3
      self.fake_sleep.assert_has_calls(
        [
            call(1),
            call(2),
        ]
      )

  def test_retries_connection_error_then_succeeds(self):
    response = Mock()
    response.status_code = 200
    operation = Mock(side_effect=[
        requests.ConnectionError(),
        response,
    ])

    result = self.policy.execute(operation)
    assert result.status_code == 200
    assert operation.call_count == 2
    self.fake_sleep.assert_called_once_with(1)