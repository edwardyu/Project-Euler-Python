"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

#The next 3 functions are copied from StackOverflow under a CC2.5 license. Author: Tyler Source: http://stackoverflow.com/a/118712/681251
import operator
# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d
def NumberOfDivisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)
  
  
def triangle(n):
    #total = 0 
    #for i in range(1, n+1):
    #    total += i
    return ((n+1)*(n)/2)    


def factors(n):
    divisors = 2
    for i in range(2, int(n**.5+1)):
        if n%i == 0:
            divisors += 1

            
    return divisors

          
def five_hundred_divisors():
    n = 1
    i = 0
    while i < 500:
        i = NumberOfDivisors(triangle(n))
        print i
        n += 1
        
    return triangle(n-1)
    
print five_hundred_divisors()
    
        
    
 
        