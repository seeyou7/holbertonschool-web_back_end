#!/usr/bin/env python3
""" Measure the runtime of asynchronous comprehensions """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """ Measure total runtime of executing async_comprehension four times in parallel """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time

