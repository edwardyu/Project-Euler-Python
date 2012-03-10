'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

def length_fibonacci(n):
    a = 1
    b = 0
    c = 0
    term = 1
    while len(str(a)) < n:
        c = a
        a += b
        term += 1
        b = c   
    return term    
    
print length_fibonacci(1000)
        
        
        

    
