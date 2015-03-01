"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143"""

#THIS ASSUMES THE EXPONENT ON HIGHEST PRIME DIVISOR IS 1

#works by effectively dividing n by primes until not divisible then
#moving on to next prime

#lots of cases fail

n = 600851475143
i = 2
while i * i < n+1:
     while n % i == 0:
         n = n / i
     i = i + 1

print (n)
