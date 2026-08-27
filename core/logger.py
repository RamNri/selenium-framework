from __future__ import annotations

import os
import logging
from pathlib import Path
from datetime import datetime
from core.execution.execution_context import ExecutionContext

class ExecutionContextFilter(logging.Filter):
  def filter(self, record: logging.LogRecord) -> bool:
    record.execution_id = ExecutionContext.execution_id()
    record.worker_id = ExecutionContext.worker_id()
    record.thread_id = ExecutionContext.thread_id()
    record.test_name = ExecutionContext.test_name()
    record.seed = ExecutionContext.seed()
    return True

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
      "%(asctime)s | "
      "%(levelname)-8s | "
      "%(name)-25s | "
      "[exec=%(execution_id)s | "
      "worker=%(worker_id)s | "
      "thread=%(thread_id)s | "
      "test=%(test_name)s | "
      "seed=%(seed)s] | "
      "%(message)s"
      ),
      datefmt="%Y-%m-%d %H:%M:%S",
    )
  
  root_logger = logging.getLogger()  #gets the root logger
  root_logger.handlers.clear()

  root_logger.setLevel(logging.INFO)

  context_filter = ExecutionContextFilter()

  #Console handler
  console_handler = logging.StreamHandler()
  console_handler.setFormatter(formatter)
  console_handler.addFilter(context_filter)


  #File handler
  file_handler = logging.FileHandler(log_file, encoding="utf-8")
  file_handler.setFormatter(formatter)
  file_handler.addFilter(context_filter)

  root_logger.addHandler(console_handler)
  root_logger.addHandler(file_handler)

  logging.getLogger().info("Logging process PID: %s", os.getpid())

  root_logger.info("=" * 80)
  root_logger.info("Logging started")

  root_logger.info(
    "Log file: %s",
    log_file.resolve()
  )

  root_logger.info("=" * 80)

  return root_logger







