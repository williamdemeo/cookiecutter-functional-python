import pytest
from core import filter_even, square

def test_filter_even():
    assert filter_even([1, 2, 3, 4, 5]) == [2, 4]

def test_square():
    assert square([1, 2, 3]) == [1, 4, 9]

if __name__ == "__main__":
    pytest.main()
