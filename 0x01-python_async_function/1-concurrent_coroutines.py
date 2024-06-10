#!/usr/bin/env python3
""" Async Function """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Return the list of all the delays (float values) """
    a_list = []
    for i in range(n):
        a_list.append(asyncio.ensure_future(wait_random(max_delay)))
        idx = []
        for completed in asyncio.as_completed(a_list):
            value = await completed
            idx.append(value)
        return idx
