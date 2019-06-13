import pytest


@pytest.mark.usefixtures('set_up', 'param')
class TestCaseOne:

    def test_one_1(self, param):
        assert param == 1

    def test_one_2(self, param):
        assert param == 2

    def test_one_3(self, param):
        assert param == 3
