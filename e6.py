# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
from math import *

def sum_of_squares(n):
    total = 0 
    for i in range(1, n+1):
        square = i**2
        total += square
    return total
    
def square_of_sums(n):
    subtotal = 0 
    total = 0 
    for i in range(1, n+1):
        subtotal += i
        total = subtotal**2
    return total 
    
answer = fabs(sum_of_squares(100)-square_of_sums(100))
print answer


