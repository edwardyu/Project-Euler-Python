# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def isprime(n):
    result = True
    for i in range(2, int(n**.5)+1):
        if n%i == 0:
            result = False
            break 
        
    return result
    
    
    
def sum_of_primes(j):
    total = 0 
    for i in range(2, j+1):
        if isprime(i)==True:
            total += i
            
    return total
        
print sum_of_primes(10)
