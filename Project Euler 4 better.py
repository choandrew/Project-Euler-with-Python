"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


#multiply two 3-digit numbers
#going to start at 900 to 999

#check number of digits
#check if palindrome

palindromes = []

for n in range(999, 899, -1):
    for m in range (999, 899, -1):
        if str(n*m)[::-1] == str(n*m):
            palindromes.append(n*m)

palindromes.sort()
print(palindromes)
