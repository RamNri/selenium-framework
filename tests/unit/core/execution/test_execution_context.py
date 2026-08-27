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