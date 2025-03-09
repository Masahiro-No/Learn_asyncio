import asyncio
# ทำ asyncio count_down
async def count_down(name, n):
    while n > 0:
        print(f"{name}: {n}")
        await asyncio.sleep(1) #จำลองว่าทำงาน 1 วินาที
        n -= 1
    print(f"{name}: Done!")