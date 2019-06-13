import pytest


@pytest.mark.usefixtures('set_up', 'param')
class TestCaseTwo:

    def test_two_1(self, param):
        assert param == 1

    def test_two_2(self, param):
        assert param == 2

    def test_two_3(self, param):
        assert param == 3
