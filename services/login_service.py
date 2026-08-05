from pages.login_page import LoginPage


class LoginService:
  def __init__(self, driver):
    self.driver = driver

  def login(self, username, password):
    return (
      LoginPage(self.driver).open().login(username, password)
    )
  
  def login_as_standard_user(self):
    return self.login(settings.USERNAME, settings.PASSWORD)