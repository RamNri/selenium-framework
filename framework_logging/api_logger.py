from __future__ import annotations

import logging
from typing import Any

from framework_logging.log_utils import LogUtils

logger = logging.getLogger("api")

class ApiLogger:
  """
  Enterprise API request/response logger.

  Responsibilites:
  -----------------
  - Log every HTTP request.
  - Log every HTTP response.
  - Pretty print JSON.
  - Mask sensitiv headers
  - Never crash because of logging.
  """
  @staticmethod
  def log_request(
    *,
    method: str,
    url: str,
    headers: dict | None = None,
    body: Any = None
  ) -> None:
    
    logger.info("=" * 100)
    logger.info("HTTP REQUEST")
    logger.info("=" * 100)

    logger.info("Method :%s", method)
    logger.info("URL    :%s", url)

    if headers:
      logger.info("Headers")

      logger.info("\n%s",LogUtils.pretty_json(LogUtils.mask_headers(headers)),)
    
    if body is not None:
      logger.info("Request Body")

      logger.info("\n%s", LogUtils.pretty_json(body),)
  
  @staticmethod
  def log_response(response) -> None:
    logger.info("_" * 100)
    logger.info("HTTP RESPONSE")
    logger.info("-" * 100)
    
    logger.info("Status code : %s", response.status_code)

    logger.info( "Reason : %s", response.reason )

    logger.info("Elapsed : %.3f sec", response.elapsed.total_seconds(),)

    logger.info("Headers")

    logger.info("\n%s", LogUtils.pretty_json(dict(response.headers)),)

    try:
      body = response.json()
      logger.info("Response Body")
      logger.info("\n%s", LogUtils.pretty_json(body),)
    
    except ValueError:
      logger.info("Response Body")
      logger.info("\n%s", response.text,)
    
    logger.info("=" * 100)