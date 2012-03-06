'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

#convert ints to string numbers
def convert(i):
    under_twenty = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven',
    'twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
    
    tens = ['', 'ten', 'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    
    if i <= 20:
        return under_twenty[i]
        
    elif 20 < i < 100:
        num = str(i)
        return tens[int(num[0])] + under_twenty[int(num[1])] 
        
    elif 100 <= i < 1000:
        num = str(i)
        a = under_twenty[int(num[0])] + 'hundred' 
        
        if num[1] != '0' or num[2] != '0':
                a += 'and'
        
        if int(num[1]) >= 2:
            b = tens[int(num[1])]
            c = under_twenty[int(num[2])]
        elif int(num[1]) < 2:
            b = under_twenty[int(num[1:])]
            c = ''
             
        
        return a + b + c
    elif i == 1000:
        return 'onethousand'
        
#find out how many letters used from 1 to 1000
total = 0
for j in range(1,1001):
    #print j
    total += len(convert(j))
    
print total

'''
Note: After reading other's code, I have realized this solution is quite bad and overly complicated. 
There are much simpler ways to do this, for example, basic math is just as easy.
'''


'''
    
    

