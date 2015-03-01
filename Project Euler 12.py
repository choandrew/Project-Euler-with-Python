import time
import math


def triangular(n):
    return (n + 1) * n / 2


start = time.time()
for i in range(7, 100000):
    number = triangular(i)
    divisors = 2
    for j in range(2, int(math.sqrt(number)) + 1):
        if not number % j:
            divisors += 2
    if divisors > 500:
        print(number)
        break

print("Elapsed time {}".format(time.time() - start))
