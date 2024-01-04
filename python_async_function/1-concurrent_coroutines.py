#!/usr/bin/env python3
"""
Define an asynchronous coroutine wait_n
"""


from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""
    _list = []
    for x in range(n):
        _list.append(await wait_random(max_delay))
    return sorted(_list)
