import time

import pytest
from selenium import webdriver

DRIVERS = [webdriver.Chrome, webdriver.Firefox]
DRIVERS_NAMES = ["Chrome", "Firefox"]


@pytest.fixture(scope="session", params=DRIVERS, ids=DRIVERS_NAMES)
def driver(request):
    driver_instance = request.param()
    yield driver_instance
    tear_down(driver_instance)


@pytest.fixture(scope="function")
def set_up(driver):
    print("\ndeleting Cookies...")
    driver.delete_all_cookies()
    driver.get("https://ammarnajjar.github.io/about/")
    time.sleep(1)
    driver.get("https://ammarnajjar.github.io/")
    time.sleep(1)


def tear_down(driver):
    driver.close()
    driver.quit()


@pytest.fixture(scope="function", params=["first", "second", "third"])
def param(request):
    yield request.param
