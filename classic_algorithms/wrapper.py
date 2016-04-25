import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(left_pad(func.__name__), end-start)
            return end-start
    return wrapper

def left_pad(s):
    return " " * (12 - len(s)) + s if len(s) < 20 else s
