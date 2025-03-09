import asyncio

async def count_down(name, n):
    while n > 0:
        print(f"{name}: {n}")
        await asyncio.sleep(1)  # จำลองการทำงานที่ใช้เวลา
        n -= 1
    print(f"{name}: Done!")

async def main():
    asyncio.create_task(count_down("⏳ Task 1", 5))
    asyncio.create_task(count_down("⏳ Task 2", 3))
    asyncio.create_task(count_down("⏳ Task 3", 4))
    print("🎉 All tasks started!")

if __name__ == "__main__":
    asyncio.run(main())
    print("🎉 All tasks done!")
