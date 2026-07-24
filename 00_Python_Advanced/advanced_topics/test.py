import asyncio


async def normal_task():
    try:
        await asyncio.sleep(10)
        print("正常完成")
    finally:
        print("normal_task 开始清理")


async def failed_task():
    await asyncio.sleep(1)
    raise RuntimeError("通信失败")


async def main():
    try:
        async with asyncio.TaskGroup() as group:
            group.create_task(normal_task())
            group.create_task(failed_task())

    except* RuntimeError as errors:
        for error in errors.exceptions:
            print(f"捕获异常：{error}")


asyncio.run(main())