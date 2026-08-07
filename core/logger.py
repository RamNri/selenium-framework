from __future__ import annotations

import logging
from pathlib import Path
from datetime import datetime

def configure_logging() -> logging.Logger:
  """
  Configure the framework logging.

  Creates
      artifacts/
              logs/
                  <timestamp>/
                             framework.log
  
  Returns:
  logging.Logger
  """

  timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  log_directory = Path("artifacts") / "logs" / timestamp
  log_directory.mkdir(parents=True, exist_ok=True)

  log_file = log_directory/ "framework.log"
  

  #It structures your log text into a clean, predictable, tabular format separated by pipes (|)

  formatter = logging.Formatter(
    fmt=(
      "%(asctime)s |"
      "%(levelname)-8s |"
      "%(name)-15s |"
      "%(message)s"
      ),
      datefmt="%Y-%m-%d %H:%M:%S",
    )
  
  root_logger = logging.getLogger()  #gets the root logger
  root_logger.handlers.clear()

  root_logger.setLevel(logging.INFO)

  #Console handler
  console_handler = logging.StreamHandler()
  console_handler.setFormatter(formatter)

  #File handler
  file_handler = logging.FileHandler(log_file, encoding="utf-8")
  file_handler.setFormatter(formatter)

  root_logger.addHandler(console_handler)
  root_logger.addHandler(file_handler)

  root_logger.info("=" * 80)
  root_logger.info("Logging started")

  root_logger.info(
    "Log file: %s",
    log_file.resolve()
  )

  root_logger.info("=" * 80)

  return root_logger







