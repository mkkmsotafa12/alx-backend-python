#!/usr/bin/env python3
""" Async Function """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Wait for a random delay between 0 and max_delay """
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
