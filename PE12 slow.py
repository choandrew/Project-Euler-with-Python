"""What is the value of the first triangle number to have over five hundred divisors?"""

import math
from functools import reduce

listofdivisors = {} #creating a dictionary of the form {prime, exponent}

n=3

while reduce(lambda x,y: x*y, map(lambda x:x+1, listofdivisors.values()),1) <= 500:
	listofdivisors = {}
	divisor=3 
	n+=1
	m = n*(n+1)/2	
	temp = m
	while 2 <= math.sqrt(temp)+1:
		if temp % 2 == 0:
			listofdivisors[2] = listofdivisors.get(2,0) + 1 #this updates the dictionary to make the value of the exponent increase by one
			temp /= 2
		else:
			break
	while divisor <= math.sqrt(temp)+1:
		if temp % divisor == 0:
			listofdivisors[divisor] = listofdivisors.get(divisor,0) + 1
			temp /= divisor
		else:
			divisor += 2

	if temp != 1:
		listofdivisors[int(temp)] = listofdivisors.get(int(temp),0) + 1




print(m, "is the first triangle number to have over five hundred divisors")
print("It is the", n, "th number and it's divisors are:", listofdivisors)
