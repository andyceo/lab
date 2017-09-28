#!/usr/bin/env python3

import asyncio


async def mycoro(number):
    print("Starting %d" % number)
    await asyncio.sleep(1)
    print("Finishing %d" % number)
    return str(number)

# We can gather many futures into one
several_futures = asyncio.gather(mycoro(1), mycoro(2), mycoro(3))
# And run it as before
loop = asyncio.get_event_loop()
print(loop.run_until_complete(several_futures))
loop.close()
