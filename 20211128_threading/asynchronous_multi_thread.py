import asyncio
#requires a .py file to run, cannot run on a notebook

async def main():
    print('a')
    await asyncio.run(thread1(1, 3))
    await asyncio.run(thread2(2, 3))

async def thread1(thread_n, sleep):
    await asyncio.sleep(sleep)
    print(thread_n)

async def thread2(thread_n, sleep):
    await asyncio.sleep(sleep)
    print(thread_n)

#do not run at the same time
asyncio.run(main())
