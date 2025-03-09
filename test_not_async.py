import time
def count_down(name, n):
    while n > 0:
        print(f"{name}: {n}")
        time.sleep(1)
        n -= 1
    print(f"{name}: Done!")

print("🎉 All tasks started!")
print(count_down("⏳ Task 1", 5))
print(count_down("⏳ Task 2", 3))
print(count_down("⏳ Task 3", 4))
print("🎉 All tasks done!")

