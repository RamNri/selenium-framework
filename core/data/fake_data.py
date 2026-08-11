from faker import Faker
from datetime import timedelta
import random
import threading

class FakeData:

  """
  Centralize enterprise test data generator.
  Every builder should use this class instead of talking directly to Faker.

  Thread-safe implementation
  """
  _context  = threading.local()

  @classmethod
  def _initialize(cls) -> None:
        """
        Creates one Faker instance per thread.
        """
        if not hasattr(cls._context, "faker"):
          cls._context.faker = Faker()
          cls.seed(random.randint(1, 999999999))

  @classmethod
  def seed(cls, value: int) -> None:
    """
    makes random test data deterministic
    """

    cls._context.faker = Faker()
    cls._context.seed = value
    cls._context.faker.seed_instance(value)

  @classmethod
  def current_seed(cls):
    """
    Returns current framework seed.
    """
    cls._initialize()
    return cls._context.seed  
    
  @classmethod
  def first_name(cls) -> str:
    cls._initialize()
    return cls._context.faker.first_name()

  @classmethod
  def last_name(cls) -> str:
    cls._initialize()
    return cls._context.faker.last_name()

  @classmethod
  def total_price(cls) -> int:
    cls._initialize()
    return cls._context.faker.random_int(min=100, max=5000)

  @classmethod
  def additional_needs(cls) -> str:
    cls._initialize()
    return cls._context.faker.random_element(
    (
        "Breakfast",
        "Lunch",
        "Dinner",
        "Baby crib",
        "Late checkout",
        "Airport pickup",
        "Extra pillow",
    )
    )

  @classmethod
  def booking_dates(cls) -> tuple[str, str]:
    cls._initialize()
    checkin = cls._context.faker.date_between(
      start_date="+1d",
      end_date="+30d"
    )

    checkout = checkin + timedelta(
      days = cls._context.faker.random_int(
        min = 1,
        max = 14,
      )
    )

    return (
      checkin.isoformat(),
      checkout.isoformat()
    )