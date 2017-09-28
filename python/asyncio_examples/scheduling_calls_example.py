import asyncio
import functools
import time


def event_handler(loop, txt, stop=False):
    print('Event handler called:' + txt)
    if stop:
        print('stopping the loop')
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.call_soon(event_handler, loop, 'loop.call_soon')
        loop.call_soon_threadsafe(event_handler, loop, 'call_soon_threadsafe')
        loop.call_later(1, event_handler, loop, 'loop.call_later(1 second)')

        current_loop_time = loop.time()
        loop.call_at(current_loop_time + 3, event_handler, loop, 'loop.call_at')

        time.sleep(5)
        loop.call_soon(functools.partial(event_handler, loop, 'loop.call_soon(with functools.partial)', stop=True))

        print('starting event loop')
        loop.run_forever()
    finally:
        print('closing event loop')
        loop.close()
