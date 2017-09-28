#!/usr/bin/env python3

import asyncio


async def mycoro(number):
    print("Starting %d" % number)
    await asyncio.sleep(1)
    print("Finishing %d" % number)
    return str(number)

myfuture1 = asyncio.ensure_future(mycoro(1))

# So we must use event loop to block waiting for a future outside of a coroutine
loop = asyncio.get_event_loop()
loop.run_until_complete(myfuture1)
loop.close()
