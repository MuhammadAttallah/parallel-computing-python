import random
import time

n = 1000000
i = 0

start_time = time.time()
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    r = x**2 + y**2

    if r <= 1:
        i += 1

pi = 4 * i/n
end_time = time.time()

print("pi=%.5f | i=%d | n=%d" % (pi, i, n))
print("time=%.5f" % (end_time - start_time))





