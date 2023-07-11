#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

async def print_yielded_values():
    async for value in async_generator():
        print(value)

asyncio.run(print_yielded_values())
