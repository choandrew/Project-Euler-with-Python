"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143"""

#the number they gave is too big too simply brute force
#b/c listing all numbers from 1 to 600851475143 causes overflow

import math
from datetime import datetime

startTime = datetime.now() #to measure speed


n = 600851475143
# if I wanted to make this interactive 
# n =  int(input("What positive integer do you want the prime factorization of?"))
factors = []
notprimefactors = []
primefactors = []

#for every factor of n under the sqrt(n), there is one
#factors of n over the sqrt(n)
#we take advantage of this fact in the below function


#this gets every factor
def factorization(p):
    for divisors in range(2,math.floor(math.sqrt(n))+1):
        if p % divisors == 0:
            factors.append(int(divisors))
            factors.append(int(p / divisors))

#this gets every nonprime factor
def getnonprimes():
    for notprime in factors:
        for ints in range(2,math.floor(math.sqrt(notprime))):
            if notprime % ints == 0:
                notprimefactors.append(notprime)

#every element of factor that is NOT in notprimefactors
#gets added to primefactors
def getprimes():
    for primes in factors:
        if primes not in notprimefactors:
            primefactors.append(primes)
        
factorization(n)
getnonprimes()
getprimes()

if primefactors == []:
    print(n)
else:
    print(max(primefactors))

print(datetime.now()-startTime)
