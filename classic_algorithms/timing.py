import time
from functools import wraps
import numpy as np

def timethis(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return end-start

def timed_calls(n, func, *args, **kwargs):
    times = [timethis(func, *args, **kwargs) for _ in range(n)]
    return min(times), np.mean(times), max(times)
