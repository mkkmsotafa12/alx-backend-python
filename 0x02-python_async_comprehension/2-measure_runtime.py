#!/usr/bin/env python3
""" Asynchronous comprehensions function """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure_runtime coroutine """
    start = time.perf_counter()
    await asyncio.gather(*([async_comprehension() for i in range(4)]))
    end = time.perf_counter()
    return end - start
