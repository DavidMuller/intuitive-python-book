import asyncio

async def sleep_then_say_hello():
    await asyncio.sleep(1)
    print("hello")

async def sleep_then_say_world():
    await asyncio.sleep(1)
    print("world")

async def main():
    # simultaneously spawn both sleep_then_say_hello and
    # sleep_then_say_world
    await asyncio.gather(sleep_then_say_hello(), sleep_then_say_world())

asyncio.run(main())
