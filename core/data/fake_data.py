from faker import Faker
from datetime import timedelta

class FakeData:

  """
  Centralize enterprise test data generator.
  Every builder should use this class instead of talking directly to Faker.
  """

  _faker = Faker()

  @classmethod
  def first_name(cls) -> str:
    return cls._faker.first_name()

  @classmethod
  def last_name(cls) -> str:
    return cls._faker.last_name()

  @classmethod
  def total_price(cls) -> int:
    return cls._faker.random_int(min=100, max=5000)

  @classmethod
  def additional_needs(cls) -> str:
    return cls._faker.random_element(
      elements=(
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
  
  
    checkin = cls._faker.date_between(
      start_date="+1d",
      end_date="+30d"
    )

    checkout = checkin + timedelta(
      days = cls._faker.random_int(
        min = 1,
        max = 15
      )
    )

    return (
      checkin.isoformat(),
      checkout.isoformat()
    )

  
  