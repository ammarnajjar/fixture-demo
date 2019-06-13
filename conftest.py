import time

import pytest
from selenium import webdriver

DRIVERS = [webdriver.Chrome, webdriver.Firefox]
DRIVERS_NAMES = ["Chrome", "Firefox"]


@pytest.fixture(scope="session", params=DRIVERS, ids=DRIVERS_NAMES)
def driver(request):
    driver = request.param()
    yield driver
    tearDown(driver)


@pytest.fixture(scope="function")
def setUp(driver):
    print("\ndeleting Cookies...")
    driver.delete_all_cookies()
    driver.get("https://ammarnajjar.github.io/about/")
    time.sleep(1)
    driver.get("https://ammarnajjar.github.io/")
    time.sleep(1)


def tearDown(driver):
    driver.close()
    driver.quit()


@pytest.fixture(scope="function", params=[1, 2, 3, 4])
def param(request):
    yield request.param
