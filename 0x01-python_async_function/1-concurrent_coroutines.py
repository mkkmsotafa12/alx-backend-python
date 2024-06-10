#!/usr/bin/env python3
""" Async Function """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays: List[float] = []
    while n > 0:
        dealy = await wait_random(max_delay)
        n -= 1
        idx = 0
        while idx < len(delays) and dealy > delays[idx]:
            idx += 1

        delays.insert(idx, dealy)

    return (delays)
