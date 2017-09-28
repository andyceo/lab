#!/usr/bin/env python3

import asyncio


async def mycoro(number):
    print("Starting %d" % number)
    await asyncio.sleep(1)
    print("Finishing %d" % number)
    return str(number)


async def print_when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print("Result %s" % await res)


coros = [mycoro(1), mycoro(2), mycoro(3)]
loop = asyncio.get_event_loop()
loop.run_until_complete(print_when_done(coros))
loop.close()
