#!/usr/bin/env python3

import asyncio


async def mycoro(number):
    print("Starting %d" % number)
    await asyncio.sleep(1)
    print("Finishing %d" % number)
    return str(number)


# We end the program without waiting for the future to finish
# Runs mycoro instead of just creating future from it!
myfuture1 = asyncio.ensure_future(mycoro(1))
