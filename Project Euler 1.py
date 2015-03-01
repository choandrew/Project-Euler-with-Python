"""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def divisible_by_3(n):
    if n % 3 == 0:
        return n

def divisible_by_5(n):
    if n % 5 == 0:
        return n


def divisible_by_both_3_and_5():
    m = 0
    for n in range(1,1000):
        if divisible_by_3(n) == n or divisible_by_5(n) == n:
            m += n
    print(m)

divisible_by_both_3_and_5()
