"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math
from datetime import datetime
startTime = datetime.now() #to measure speed


n = 10001
# int(input("What number prime do you want? "))
primes = [2]

m = 3

while len(primes) < n:
    a = []
    for divisors in range(2,math.floor(math.sqrt(m))+1):
        a.append(m % divisors != 0)   
    if all(a) == True:
        primes.append(m)
    m += 2


print(primes[-1])
print(datetime.now()-startTime)
