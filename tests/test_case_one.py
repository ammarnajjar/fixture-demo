import pytest


@pytest.mark.usefixtures('setUp', 'param')
class TestCaseOne:

    def test_one_1(self, param):
        assert 1 == param

    def test_one_2(self, param):
        assert 2 == param

    def test_one_3(self, param):
        assert 3 == param
