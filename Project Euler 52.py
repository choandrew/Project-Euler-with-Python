"""It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits. """

#I tried to avoid using string methods in this solution

import math

foundnumber = False

digits = 5

def makearray(number):
    array = []
    for iteration in range(int(math.log10(number)+1)):
        #this is the process that puts the digits into the array by iterating
        
        array.append(number % 10)
        number //= 10
        #that double slash is integer division, which I had to  use, because I needed integer outputs
        #apparently, a single slash in python gets float division
    return array

def checkarray(array1, array2):
        #now I will check if array1 has the same numbers as array2
        for digit in array1:
            if digit not in array2:
                return False
        return True

while foundnumber == False:
    for numbers1 in range(10 ** digits, (10 ** (digits + 1))//6):
        #the reason I'm only checking up to 10 ** (digits + 1)/6, which is equal to 1 followed by 6s (aka 16, 166, 1666, 16666) is because
        #6x needs to have the same number of digits as x
        #so for example x = 167 would not work because 167 * 6 = 1001 has one more digits

        a=makearray(numbers1)
        b=makearray(numbers1*2)
        c=makearray(numbers1*3)
        d=makearray(numbers1*4)
        e=makearray(numbers1*5)
        f=makearray(numbers1*6)
      

        if checkarray(a,b) == checkarray(a,c) == checkarray(a,d) == checkarray(a,f) == checkarray(a,f) == True:
            print(numbers1)
            foundnumber = True

    digits += 1
