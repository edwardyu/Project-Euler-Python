# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
def products(): #create a list of all possible products
    numbers = []
    for i in range(100, 1000):
        for n in range(100, 1000):
             
            numbers.append(i * n)
    return numbers        
            
def palindrome(numbers): #check the palindromes in the list of all products
    best = 0 
    for i in numbers:
        p = str(i)
        if len(p)==6 and p[0]==p[5] and p[1]==p[4] and p[2]==p[3]:
            if i > best: #only keep the highest number
                best = i 
    print best        
num = products()
palindrome(num)
