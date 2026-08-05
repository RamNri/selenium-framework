class FrameworkException(Exception):
  """Base Exception for the automation framework"""
  """Every framework specific exception can inherit from this"""

class ElementNotFoundError(FrameworkException):
  """Raised when an expected element cannot be located"""
  def __init__(self, locator, page_name, timeout, current_url, page_title):
    self.locator = locator
    self.page_name = page_name
    self.timeout = timeout
    self.current_url = current_url
    self.page_title = page_title

    super().__init__(
      f"Element{locator} was not found on"
      f"{page_name} after {timeout} seconds"
    )

  
