from core.data.fake_data import FakeData

class TestFakeDataSeed:

  def test_first_name_returns_string(self):
    assert isinstance(FakeData.first_name(), str,)

  def test_last_name_returns_string(self):
    assert isinstance(FakeData.last_name(), str,)

  def test_total_price_range(self):
    price = FakeData.total_price()
    assert 100 <= price <=5000

  def test_seed_generates_same_name(self):

    FakeData.seed(100)
    first = FakeData.first_name()

    FakeData.seed(100)
    second = FakeData.first_name()

    assert first == second

  def test_seed_generates_same_date(self):
    FakeData.seed(100)
    first = FakeData.booking_dates()

    FakeData.seed(100)
    second = FakeData.booking_dates()

    assert first == second

  def test_seed_generates_same_price(self):
    FakeData.seed(100)
    first = FakeData.total_price()

    FakeData.seed(100)
    second = FakeData.total_price()

    assert first == second
  
  def test_initialize_creates_seed(self):

    FakeData._seed = None
    FakeData.first_name()

    assert FakeData.current_seed() is not None