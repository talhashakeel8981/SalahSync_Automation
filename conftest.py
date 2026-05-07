import pytest
from utils.driver_utils import create_driver




@pytest.fixture(scope="function")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()