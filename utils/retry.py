"""
memory util module
make a util to calculate memory usage of a process or system, and so on.
"""
from typing import Optional


import time
from functools import wraps

def retry(retries: Optional[int]=1, interval: Optional[int]=1, backoff: Optional[int]=2, on_exception: Optional[Exception]=Exception):
    """
    :param retries: 最大重试次数。
    :param interval: 重试前的等待时间（以秒为单位）。
    :param backoff: 每次重试的延迟时间翻倍的因子
    :returns: callable
    """
    def decorator_retry(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = retries
            delay = interval
            # 按照设定次数尝试
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except on_exception:
                    # 出现指定异常进行重试
                    attempts -= 1
                    if attempts > 0:
                        time.sleep(delay)
                        delay *= backoff
                    else:
                        raise
        return wrapper
    return decorator_retry