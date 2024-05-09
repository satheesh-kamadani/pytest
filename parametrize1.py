import pytest

@pytest.mark.parametrize("n, expected", [(1, 2), (3, 4)])
class TestClass:
    def test_simple_test(self, n, expected):
        assert n + 1 == expected

    def test_wired_example(self, n, expected):
        assert (n * 1) + 1 == expected

