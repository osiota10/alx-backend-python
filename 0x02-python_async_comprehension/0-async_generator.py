#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

async def consume_async_generator():
    async for value in async_generator():
        print(value)

loop = asyncio.get_event_loop()
loop.run_until_complete(consume_async_generator())
