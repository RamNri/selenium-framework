from enum import Enum

class Browser(str, Enum):
  CHROME = "chrome"
  FIREFOX = "firefox"
  EDGE = "edge"