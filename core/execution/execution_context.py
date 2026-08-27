from __future__ import annotations
from faker import Faker

import threading
import uuid
import random
from datetime import datetime


class ExecutionContext:
  """
  Stores execution information for current thread.
  Every parallel test gets its own context.
  """

  _context = threading.local()

  @classmethod
  def initialize(cls) -> None:
    if hasattr(cls._context, "initialized"):
      return

    cls._context.initialized = True
  
    cls._context.execution_id = (uuid.uuid4().hex)

    cls._context.worker_id = None

    cls._context.thread_id = (threading.get_ident())

    cls._context.started_at = (datetime.now())

    cls._context.seed = random.randint(1, 999999999)
    cls._context.faker = Faker()
    cls._context.faker.seed_instance(cls._context.seed)

    cls._context.driver = None

    cls._context.test_name = None

    cls._context.browser = None
    cls._context.session_id = None

  @classmethod
  def start_test(cls, test_name: str | None = None) -> None:
    cls.initialize()

    cls._context.execution_id = uuid.uuid4().hex
    cls._context.started_at = datetime.now()

    cls._context.seed = random.randint(1, 999999999)

    cls._context.faker = Faker()
    cls._context.faker.seed_instance(cls._context.seed)

    cls._context.test_name = test_name

    cls._context.driver = None
    cls._context.browser = None
    cls._context.session_id = None
   
  @classmethod
  def execution_id(cls):
    cls.initialize()
    return cls._context.execution_id

  @classmethod
  def worker_id(cls):
    cls.initialize()
    return cls._context.worker_id

  @classmethod
  def set_worker_id(cls, value):
    cls.initialize()
    cls._context.worker_id = value

  @classmethod
  def thread_id(cls):
    cls.initialize()
    return cls._context.thread_id

  @classmethod
  def started_at(cls):
    cls.initialize()
    return cls._context.started_at

  @classmethod
  def seed(cls):
    cls.initialize()
    return cls._context.seed

  @classmethod
  def set_seed(cls, value):
    cls.initialize()
    cls._context.seed = value

  @classmethod
  def driver(cls):
    cls.initialize()
    return cls._context.driver

  @classmethod
  def set_driver(cls, driver):
    cls.initialize()
    cls._context.driver = driver

  @classmethod
  def test_name(cls):
    cls.initialize()
    return cls._context.test_name

  @classmethod
  def set_test_name(cls, name):
    cls.initialize()
    cls._context.test_name = name

  @classmethod
  def faker(cls):
    cls.initialize()
    return cls._context.faker

  @classmethod
  def reset_faker(cls):
    cls.initialize()
    cls._context.faker = Faker()
    cls._context.faker.seed_instance(cls._context.seed)

  @classmethod
  def duration(cls):
    cls.initialize()
    return (datetime.now() - cls._context.started_at).total_seconds()

  @classmethod
  def browser(cls):
    cls.initialize()
    return cls._context.browser

  @classmethod
  def set_browser(cls, value):
    cls.initialize()
    cls._context.browser = value

  @classmethod
  def session_id(cls):
    cls.initialize()
    return cls._context.session_id

  @classmethod
  def set_session_id(cls, value):
    cls.initialize()
    cls._context.session_id = value
