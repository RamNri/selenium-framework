from datetime import date
from core.data.fake_data import FakeData
from concurrent.futures import ThreadPoolExecutor

def worker(seed):
  FakeData.seed(seed)
  return FakeData.current_seed()

class TestFakeData:

  """
  Since FakeData generates random data, we are checking type, range and business rules
  """

  def test_first_name(self):
    assert isinstance(FakeData.first_name(), str)

  def test_last_name(self):
    assert isinstance(FakeData.last_name(), str)

  def test_total_price(self):
    price = FakeData.total_price()
    assert 100 <= price <= 5000

  def test_booking_dates(self):
    checkin, checkout = (FakeData.booking_dates())
    checkin = date.fromisoformat(checkin)
    checkout = date.fromisoformat(checkout)

    assert checkout > checkin

  def test_additional_needs(self):
    assert(
      FakeData.additional_needs is not None
    )

  def test_thread_local_seed(self):
    with ThreadPoolExecutor(max_workers=2) as executor:
      results = list(executor.map(worker, [100, 200],))

    assert results == [100, 200]
    