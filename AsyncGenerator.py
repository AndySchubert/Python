import asyncio

async def generator(n):
    for i in range(n):
        yield i
        await asyncio.sleep(0.1)

async def main():
    async for i in generator(10):
        print(i)

asyncio.run(main())