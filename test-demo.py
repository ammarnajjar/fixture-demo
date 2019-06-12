import pytest
from selenium import webdriver

DRIVERS = [webdriver.Chrome, webdriver.Firefox]
DRIVERS_NAMES = ["Chrome", "Firefox"]


@pytest.fixture(scope="module", params=DRIVERS, ids=DRIVERS_NAMES)
def driver(request):
    driver = request.param()
    yield driver
    tearDown(driver)


@pytest.fixture(scope="function")
def setUp(driver):
    print("\ndeleting Cookies...")
    driver.delete_all_cookies()
    driver.get(
        "https://entwweb.eventim-inhouse.de/phoenixentw/webticket/shop?mandant=TAU&kassierer=web")
    driver.get("https://ammarnajjar.github.io/")


def tearDown(driver):
    driver.close()
    driver.quit()


@pytest.fixture(scope="function", params=[1, 2, 3, 4])
def param(request):
    yield request.param


@pytest.mark.usefixtures('setUp', 'param')
class TestCaseOne:

    def test_1(self, param):
        assert 1 == param

    def test_2(self, param):
        assert 2 == param

    def test_3(self, param):
        assert 3 == param
