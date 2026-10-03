import asyncio
import time

async def task1():
    print(f"task1开始")
    await asyncio.sleep(5)
    print(f"task1结束")
    return "task1"

async def task2():
    print(f"task2开始")
    await asyncio.sleep(2)
    print(f"task2结束")
    return "task2"

async def main():
    event_loop = asyncio.get_running_loop()
    res1 = event_loop.create_task(task1())
    res2 = event_loop.create_task(task2())
    print(await res1,await res2)
    # res = await asyncio.gather(task1(), task2())
    # print(res)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f"耗时:{time.time() - start:.2f}")
