#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2**1000?

number = str(2**1000)
 

def sum_of_digits(n):
    total = 0
    for i in range(0, len(number)):
        total += int(number[i])
    return total
    
print sum_of_digits(number)
    
