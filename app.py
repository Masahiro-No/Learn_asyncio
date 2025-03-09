import asyncio
# ทำ asyncio count_down
async def count_down(name, n):
    while n > 0:
        print(f"{name}: {n}")
        await asyncio.sleep(1) #จำลองว่าทำงาน 1 วินาที
        n -= 1
    print(f"{name}: Done!")

async def main():
    task1 = asyncio.create_task(count_down("⏳ Task 1", 5))
    task2 = asyncio.create_task(count_down("⏳ Task 2", 3))
    task3 = asyncio.create_task(count_down("⏳ Task 3", 4))
    print("🎉 All tasks started!")

    await task1 #ใช้เพื่อให้ task ทำงานเสร็จก่อนในแต่ล่ะ loop ถ้าไม่มีจะทำให้ ยังไม่ได้ print ว่านับเสร็จแล้ว แต่กระบวนการข้างหลังเสร็จไปแล้ว
    await task2
    await task3

if __name__ == "__main__":
    asyncio.run(main())
    print("🎉 All tasks done!")
