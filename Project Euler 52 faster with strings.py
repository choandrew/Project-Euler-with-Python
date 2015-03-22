"""It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits. """

#faster implementation of previous solution using string methods

f = lambda n:sorted(str(n))

n = 99999
while not f(n*2) == f(n*3) == f(n*4) == f(n*5) == f(n*6):
    n += 9

print(n)
