from typing import List, Callable
from functools import reduce

def filter_even(numbers: List[int]) -> List[int]:
    """Filters even numbers from the list."""
    return list(filter(lambda x: x % 2 == 0, numbers))

def square(numbers: List[int]) -> List[int]:
    """Squares each number in the list."""
    return list(map(lambda x: x ** 2, numbers))

def double(numbers: List[int]) -> List[int]:
    """Doubles each number in the list."""
    return list(map(lambda x: x * 2, numbers))

def filter_greater_than(numbers: List[int], threshold: int) -> List[int]:
    """Filters numbers greater than a given threshold."""
    return list(filter(lambda x: x > threshold, numbers))

def sum_squares(numbers: List[int]) -> int:
    """Computes the sum of squares using reduce."""
    return reduce(lambda acc, x: acc + x, numbers, 0)

def compose(*funcs: Callable) -> Callable:
    """Composes multiple functions from right to left."""
    def composed_function(data):
        for f in reversed(funcs):
            data = f(data)
        return data
    return composed_function
