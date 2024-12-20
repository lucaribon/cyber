import random
import sys
import time

tup = (2019, 5, 5, 9, 9, 38, 6, 125, 0)
cur_time = str(time.mktime(tup)).encode('ASCII')
random.seed(cur_time)

with open("top_secret", "r") as f:
    file = f.read()

key = [random.randrange(256) for _ in file]
msg = [m ^ k for (m,k) in zip(file.encode('ASCII') + cur_time, key + [0x88]*len(cur_time))]

print("msg:", msg)