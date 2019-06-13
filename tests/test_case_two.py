import pytest


@pytest.mark.usefixtures('setUp', 'param')
class TestCaseTwo:

    def test_two_1(self, param):
        assert 1 == param

    def test_two_2(self, param):
        assert 2 == param

    def test_two_3(self, param):
        assert 3 == param
