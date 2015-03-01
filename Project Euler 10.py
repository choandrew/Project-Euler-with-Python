"""Find the sum of all the primes below two million."""
import math

#very similar to problem 7

n = 2000000


primes = [2]
m = 3

s = 0


while primes[-1] < n:
    a = []
    for divisors in range(2,math.floor(math.sqrt(m))+1):
        a.append(m % divisors != 0)   
    if all(a) == True:
        if m < 2000000:
            print(m)
            primes.append(m)
            s += m
    m += 2

print(s)


#I realized after the fact that
#the dependency of this program on the list "primes"
#makes it extremely inefficient, as the list gets huge
