#Find the sum of all the multiples of 3 or 5 below 1000.

def check_multiple(n): #checks if number is multiple of 3 or 5
    if n%3 == 0 or n%5 == 0:
        return True
    else:
        return False
        
def add_multiples(i):
    total = 0
    for j in range(1, i):
        if check_multiple(j):
            total += j
    print total    
            
add_multiples(1000)    
