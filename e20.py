def factorial(n):
    product = 1
    for i in range(1, n+1):
        product *= i
        
    return product
    
def sum_of_digits(num):
    total = 0
    num = str(num)
    for i in num:
        
        total += int(i)
        
    return total
    
print sum_of_digits(factorial(100))
        
