"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

#this is 100% brute force
import math

a=1
b=1
while a + b + math.sqrt(a**2 + b**2) != 1000:
    print(a,b, a + b + math.sqrt(a**2 + b**2))
    if a + b + math.sqrt(a**2 + b**2) < 1000:
        a+=1
    elif a + b + math.sqrt(a**2 + b**2) > 1000:
        a=1
        b+=1
    else:
        break
    
print(a,b, math.sqrt(a**2 + b**2))


""" or you can do this:

for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            if i<j<k and i*i + j*j == k*k and i+j+k == 1000:
                print(i, j , k)
                print(i*j*k)
"""
