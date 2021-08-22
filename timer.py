import time, sys
a = 0
Time = int(input("Set a timer here in seconds: "))

for i in range(Time, 0, -1):
    print(i)
    time.sleep(1)
print("Your timer is complete.")
sys.exit()
