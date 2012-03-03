#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def prime_factors(n):
    yes = 0
    i = 2
    while i <= n:
        if n%i == 0:
            n = n/i
            
            print i
        i += 1
            
    
    
prime_factors(465837)
            
        
