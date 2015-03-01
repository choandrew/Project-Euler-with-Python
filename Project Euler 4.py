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
        #following lines will check for number of digits of n*m
        #when n and m > 900 its always going to be 6, but just for kicks
        if len(str(n*m)) == 6:
            if str(n*m)[0] == str(n*m)[5] and str(n*m)[1] == str(n*m)[4] and str(n*m)[2] == str(n*m)[3]:
                palindromes.append(n*m)
        elif len(str(n*m)) == 5:
            if str(n*m)[0] == str(n*m)[4] and str(n*m)[1] == str(n*m)[3]:
                palindromes.append(n*m)
        else:
            print("SOMETHING WENT WRONG, AHHH!!!!!!")

palindromes.sort()
print(palindromes)
