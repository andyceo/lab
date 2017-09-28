#!/usr/bin/env python3

import asyncio


async def f2():
    print("start f2")
    await asyncio.sleep(1)
    print("stop f2")


async def f1():
    print("start f1")
    await f2()
    print("stop f1")


loop = asyncio.get_event_loop()
loop.run_until_complete(f1())
loop.close()
