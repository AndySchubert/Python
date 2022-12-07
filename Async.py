import asyncio

# Async best suited for tasks which involve Web service calls, Database query calls etc
# Threads are more for process intensive tasks

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)
    print("Done fetching")
    return [1,2,3,4,5,6]

async def run_algorithm():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    # data = await.fetch_data()
    # await run_algorithm()
    # print(await data)
    data = await asyncio.gather(fetch_data(), run_algorithm()) # data is called a future

asyncio.run(main())