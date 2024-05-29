# linear search
import random
import time
from datetime import datetime

data = [1, 1, 6, 13, 14, 14, 23, 23, 26, 26, 30, 31, 32, 32, 37, 42, 44, 47, 48, 50]
# for i in range(20):
#     data.append(random.randint(1, 50))
# print(data)
target = int(input("target = "))
count = 0
print(datetime.now())
for j in data:
    time.sleep(1)
    count += 1
    if j == target:
        print(target)
        break
print(count)
print(datetime.now())
