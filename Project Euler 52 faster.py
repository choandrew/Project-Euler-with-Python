"""It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits. """

#faster implementation of previous solution without using string methods
import math
def makearray(number):
    array = []
    for iteration in range(int(math.log10(number)+1)):
        #this is the process that puts the digits into the array by iterating
        
        array.append(number % 10)
        number //= 10
        #that double slash is integer division,
        #which I had to  use, because I needed integer outputs
        #apparently, a single slash in python gets float division
    return array


f = lambda n:sorted(makearray(n))

n = 99999
while not f(n*2) == f(n*3) == f(n*4) == f(n*5) == f(n*6):
	n += 1
	if n == 999999999999:
		break

print(n)
