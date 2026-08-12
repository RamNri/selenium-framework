from core.execution.execution_context import ExecutionContext

class TestExecutionContext:

  def test_execution_id_exists(self):
    assert (ExecutionContext.execution_id() is not None)

  def test_thread_id_exists(self):
    assert(ExecutionContext.thread_id is not None)

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
