import threading
from core.execution.execution_context import ExecutionContext
from datetime import datetime, timedelta

class TestExecutionContext:

  def test_execution_id_exists(self):
    assert (ExecutionContext.execution_id() is not None)

  def test_thread_id_exists(self):
    assert(ExecutionContext.thread_id() is not None)

  def test_seed(self):
    ExecutionContext.set_seed(100)
    assert(ExecutionContext.seed() == 100)
  
  def test_driver(self):
    driver = object()
    ExecutionContext.set_driver(driver)
    assert (ExecutionContext.driver() is driver)

  def test_test_name(self):
    ExecutionContext.set_test_name("booking")
    assert(ExecutionContext.test_name() == "booking")

  def test_worker_id(self):
    ExecutionContext.set_worker_id("gw0")
    assert ExecutionContext.worker_id() == "gw0"

  def test_duration_is_calculated_from_current_test_start(self, monkeypatch):
    ExecutionContext.start_test("test_duration")

    start_time = datetime(2026, 1, 1, 10, 0, 0)
    monkeypatch.setattr(ExecutionContext._context,
                        "started_at",
                        start_time)
    current_time = start_time + timedelta(seconds=5)

    class FixedDataTime:
      @classmethod
      def now(cls):
        return current_time

    monkeypatch.setattr(
       "core.execution.execution_context.datetime",
       FixedDataTime,
    )

    assert ExecutionContext.duration() == 5.0

  def test_start_test_creates_new_execution_id(self):
    ExecutionContext.start_test("test_a")
    execution_id_a = ExecutionContext.execution_id()

    ExecutionContext.start_test("test_b")
    execution_id_b = ExecutionContext.execution_id()

    assert execution_id_a != execution_id_b

  def test_start_test_updates_test_name(self):
    ExecutionContext.start_test("test_a")
    assert ExecutionContext.test_name() == "test_a"
    ExecutionContext.start_test("test_b")
    assert ExecutionContext.test_name() == "test_b"

  def test_start_test_resets_started_at(self):
    ExecutionContext.start_test("test_a")
    started_at_a = ExecutionContext.started_at()

    ExecutionContext.start_test("test_b")
    started_at_b = ExecutionContext.started_at()

    assert started_at_b >= started_at_a

  def test_multiple_tests_can_run_on_same_thread(self):
    ExecutionContext.start_test("test_a")
    thread_a = ExecutionContext.thread_id()
    execution_a = ExecutionContext.execution_id()

    ExecutionContext.start_test("test_b")
    thread_b = ExecutionContext.thread_id()
    execution_b = ExecutionContext.execution_id()

    assert thread_a == thread_b
    assert execution_a != execution_b

  def test_start_test_does_not_change_worker_id(self):
    ExecutionContext.set_worker_id("gw0")

    ExecutionContext.start_test("test_a")
    worker_a = ExecutionContext.worker_id()

    ExecutionContext.start_test("test_b")
    worker_b = ExecutionContext.worker_id()

    assert worker_a == "gw0"
    assert worker_b == "gw0"

  def test_start_test_clears_previous_driver_context(self):
    driver = object()

    ExecutionContext.set_driver(driver)
    ExecutionContext.set_browser("chrome")
    ExecutionContext.set_session_id("session-123")
    ExecutionContext.start_test("test_b")

    assert ExecutionContext.driver() is None
    assert ExecutionContext.browser() is None
    assert ExecutionContext.session_id() is None

  def test_execution_context_is_isolated_between_threads(self):

    results = {}

    def worker(name, browser, session_id):

        ExecutionContext.start_test(name)

        ExecutionContext.set_browser(browser)
        ExecutionContext.set_session_id(session_id)

        results[name] = {
            "test_name": ExecutionContext.test_name(),
            "browser": ExecutionContext.browser(),
            "session_id": ExecutionContext.session_id(),
            "thread_id": ExecutionContext.thread_id(),
        }

    thread_a = threading.Thread(
        target=worker,
        args=("test_a", "chrome", "session-a"),
    )

    thread_b = threading.Thread(
        target=worker,
        args=("test_b", "firefox", "session-b"),
    )

    thread_a.start()
    thread_b.start()

    thread_a.join()
    thread_b.join()

    assert results["test_a"]["test_name"] == "test_a"
    assert results["test_a"]["browser"] == "chrome"
    assert results["test_a"]["session_id"] == "session-a"

    assert results["test_b"]["test_name"] == "test_b"
    assert results["test_b"]["browser"] == "firefox"
    assert results["test_b"]["session_id"] == "session-b"

    assert (
        results["test_a"]["thread_id"]
        != results["test_b"]["thread_id"]
    )

  def test_reset_faker_recreates_deterministic_faker(self):

    ExecutionContext.set_seed(12345)
    ExecutionContext.reset_faker()

    first_faker = ExecutionContext.faker()
    first_value = first_faker.name()

    ExecutionContext.reset_faker()

    second_faker = ExecutionContext.faker()
    second_value = second_faker.name()

    assert first_faker is not second_faker

    assert first_value == second_value

  def test_start_test_creates_new_faker_instance(self):

    ExecutionContext.start_test("test_a")

    faker_a = ExecutionContext.faker()

    ExecutionContext.start_test("test_b")

    faker_b = ExecutionContext.faker()

    assert faker_a is not faker_b

  def test_start_test_resets_test_state_and_preserves_worker_state(self):

    ExecutionContext.set_worker_id("gw0")
    original_thread_id = ExecutionContext.thread_id()

    ExecutionContext.set_driver(object())
    ExecutionContext.set_browser("chrome")
    ExecutionContext.set_session_id("session-123")
    ExecutionContext.set_test_name("old_test")

    old_execution_id = ExecutionContext.execution_id()

    ExecutionContext.start_test("new_test")

    assert ExecutionContext.worker_id() == "gw0"
    assert ExecutionContext.thread_id() == original_thread_id

    assert ExecutionContext.test_name() == "new_test"
    assert ExecutionContext.execution_id() != old_execution_id

    assert ExecutionContext.driver() is None
    assert ExecutionContext.browser() is None
    assert ExecutionContext.session_id() is None

  def test_initialize_does_not_reset_existing_context_state(self):

    ExecutionContext.set_worker_id("gw0")
    ExecutionContext.set_test_name("booking_test")
    ExecutionContext.set_browser("chrome")
    ExecutionContext.set_session_id("session-123")

    original_execution_id = ExecutionContext.execution_id()
    original_started_at = ExecutionContext.started_at()
    original_seed = ExecutionContext.seed()

    ExecutionContext.initialize()

    assert ExecutionContext.worker_id() == "gw0"
    assert ExecutionContext.test_name() == "booking_test"
    assert ExecutionContext.browser() == "chrome"
    assert ExecutionContext.session_id() == "session-123"

    assert ExecutionContext.execution_id() == original_execution_id
    assert ExecutionContext.started_at() == original_started_at
    assert ExecutionContext.seed() == original_seed