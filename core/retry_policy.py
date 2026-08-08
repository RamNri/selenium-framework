from __future__ import annotations
from typing import Callable

import logging
import time
import requests

logger = logging.getLogger(__name__)

class RetryPolicy:
  """
  Enterprise retry mechanism

  Retries
   - Network timeouts
   - Connection errors
   - configurable HTTP status codes
  """
  def __init__(self, retries: int, delay: float, backoff: float, retry_status_codes: set[int], sleeper=time.sleep,):
    self._retries = retries
    self._delay = delay
    self._backoff = backoff
    self._retry_status_codes = retry_status_codes
    self._sleeper = sleeper

  def execute(self, operation: Callable, ):
    delay = self._delay
    last_exception = None
    response = None

    for attempt in range(1, self._retries + 1):
      should_retry = False

      try:
          response = operation()
          #Successful resposne
          if (response.status_code not in self._retry_status_codes):
            return response
        
          logger.warning("Retryable status code %s receieved", response.status_code,)
          should_retry = True

      except ( requests.ConnectionError, requests.Timeout,) as ex:
          last_exception = ex
          logger.warning("Network exception: %s", ex,)
          should_retry = True
       
      if not should_retry:
          return response

      if attempt == self._retries:
          break

      logger.info("Retry %s/%s after %.1f sec", attempt, self._retries, delay,)
      self._sleeper(delay)
      delay *= self._backoff

    #Raise last exception if we had one
    if last_exception:
       raise last_exception
    
    #otherwise return final response
    return response 