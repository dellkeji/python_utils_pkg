"""
decorators module
make a decorator to render the function or class methods
"""

import random
import functools
import time
from typing import Callable


def sample(sample_rate: float) -> Callable:
    """
    Usage:

    >>> @sample(0.5)
    ... def demo_function(*args, **kwargs):
    ...     return 1
    """

    def _sample(function: Callable) -> Callable:
        @functools.wraps(function)
        def __sample(*args, **kwargs):
            if random.random() < sample_rate:
                return function(*args, **kwargs)
            else:
                return None

        return __sample

    return _sample


def cost_time(function: Callable) -> Callable:
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"{function.__name__} 函数执行时间：{end_time - start_time} 秒")
        
        return result
    return wrapper