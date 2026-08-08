BASE_URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
TIMEOUT = 10
API_BASE_URL='https://restful-booker.herokuapp.com'
REQUEST_TIMEOUT = 30
API_USERNAME = "admin"
API_PASSWORD = "password123"
MAX_API_RESPONSE_TIME = 5
MAX_RETRIES = 3
RETRY_DELAY = 1  #SECONDS
RETRY_BACKOFF = 2  #EXPONENTIAL MULTIPLIER

RETRY_STATUS_CODES = {
  500,  #Internal server error
  502,  #Bad Gateway
  503,  #Service Unavailable
  504   #Gateway timeout
}