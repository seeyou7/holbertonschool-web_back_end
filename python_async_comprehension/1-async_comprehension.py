#!/usr/bin/env python3
""" Define Async Comprehensions"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return 10 random float numbers"""
    return [num async for num in async_generator()]
