import pytest
from test_data.login_data import LOGIN_USERS
from services.login_service import LoginService

@pytest.mark.parametrize(
    "username,password",
    LOGIN_USERS,
     ids=[

        "Standard User",

        "Problem User",

        "Performance User",

        "Locked User"

    ]
)

def test_login(driver, username, password):
  inventory = ( 
    LoginService(driver).login(username, password)
  )
  assert inventory.is_loaded()