'''
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

        
def sequence(num):
    terms = 0
    while num != 1:
        if num%2 == 0:
            terms += 1
            num = num/2
        else:
            terms += 1
            num = 3*num + 1
            
    return terms

best = 0   
answer = 0 
for i in range(999999, 500001, -2):
    length = sequence(i)
    if length > best:
        best = length
        answer = i
        print answer 
        
print answer
            
    
