from pathlib import Path

#Root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

#Test data
TEST_DATA = PROJECT_ROOT / "test_data"

STATIC_DATA = TEST_DATA / "static"
DYNAMIC_DATA = TEST_DATA / "dynamic"

#Booking datasets
DEFAULT_BOOKING = STATIC_DATA / "booking.json"
UPDATE_BOOKING = STATIC_DATA / "update_booking.json"
INVALID_BOOKING = STATIC_DATA / "invalid_booking.json"

#Reports
REPORTS = PROJECT_ROOT / "reports"

#Logs
LOGS = PROJECT_ROOT/ "logs"

#Screenshots
SCREENSHOTS = PROJECT_ROOT / "screenshots"
