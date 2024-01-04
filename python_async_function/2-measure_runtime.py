#!/usr/bin/env python3
"""
Define measure_time
"""


import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure the total execution time for wait_n(n, max_delay)"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total = end_time - start_time
    average = total / n
    return average
