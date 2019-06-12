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


@pytest.mark.usefixtures('setUp')
class TestCaseOne:

    def test_1(self):
        assert 1

    def test_2(self):
        assert 1

    def test_3(self):
        assert 1

    def test_4(self):
        assert 1

    def test_5(self):
        assert 1

    def test_6(self):
        assert 1

    def test_7(self):
        assert 1

    def test_8(self):
        assert 1

    def test_9(self):
        assert 1

    def test_10(self):
        assert 1

    def test_11(self):
        assert 1

    def test_12(self):
        assert 1

    def test_13(self):
        assert 1

    def test_14(self):
        assert 1

    def test_15(self):
        assert 1

    def test_16(self):
        assert 1

    def test_17(self):
        assert 1

    def test_18(self):
        assert 1

    def test_19(self):
        assert 1

    def test_20(self):
        assert 1

    def test_21(self):
        assert 1

    def test_22(self):
        assert 1

    def test_23(self):
        assert 1

    def test_24(self):
        assert 1
