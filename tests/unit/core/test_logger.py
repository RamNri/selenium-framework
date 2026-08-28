import logging
from core.logger import ExecutionContextFilter
from core.execution.execution_context import ExecutionContext

class TestExecutionContextFilter:

  def test_filter_adds_execution_context(self):

    ExecutionContext.set_worker_id("gw0")
    ExecutionContext.set_test_name("test_example")
    ExecutionContext.set_browser("chrome")
    ExecutionContext.set_session_id("session-123")

    record = logging.LogRecord(
      name="test",
      level=logging.INFO,
      pathname=__file__,
      lineno=1,
      msg="hello",
      args=(),
      exc_info=None,
    )

    context_filter = ExecutionContextFilter()

    result = context_filter.filter(record)
    assert result is True

    assert record.execution_id == (ExecutionContext.execution_id())
    assert record.worker_id == "gw0"
    assert record.thread_id == (ExecutionContext.thread_id())
    assert record.test_name == "test_example"
    assert record.seed == (ExecutionContext.seed())
    assert record.browser == "chrome"
    assert record.session_id == "session-123"
    