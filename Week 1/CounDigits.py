num = 5438
count = 0
while num>0:
    count +=1 
    num = num // 10
print(count)

from math import *

def countDigits(num):
    return int (log10(num)) + 1

print( countDigits(5438) )

# TC O(log10(n))
# SC O(1)