from faker import Faker
from datetime import timedelta
from core.execution.execution_context import ExecutionContext
import random
import threading

class FakeData:

  """
  Centralize enterprise test data generator.
  Every builder should use this class instead of talking directly to Faker.

  Thread-safe implementation
  """

  @classmethod
  def seed(cls, value: int) -> None:
    """
    makes random test data deterministic
    """
    ExecutionContext.set_seed(value)
    ExecutionContext.reset_faker()
 

  @classmethod
  def current_seed(cls):
    """
    Returns current framework seed.
    """
    return ExecutionContext.seed()
  
  @classmethod
  def first_name(cls) -> str:
    return ExecutionContext.faker().first_name()

  @classmethod
  def last_name(cls) -> str:
    return ExecutionContext.faker().last_name()

  @classmethod
  def total_price(cls) -> int:

    return ExecutionContext.faker().random_int(min=100, max=5000)

  @classmethod
  def additional_needs(cls) -> str:
    return ExecutionContext.faker().random_element(
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
    checkin = ExecutionContext.faker().date_between(
      start_date="+1d",
      end_date="+30d"
    )

    checkout = checkin + timedelta(
      days = ExecutionContext.faker().random_int(
        min = 1,
        max = 14,
      )
    )

    return (
      checkin.isoformat(),
      checkout.isoformat()
    )