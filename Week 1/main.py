# Variables are dynamically typed in Python
n = 0
print('n = ',n)

n="abc"
n = 0

n= n+1
n +=1

if n > 2:
    n -=1
elif n == 2:
    n *=2
else:
    n /=2
    
# and or
if(n > 2 and n < 10):
    print('n is between 2 and 10')

# looping from i=0 to i=4
for i in range(5):
    print(i)

for i in range(2,5):
    print(i)

for i in range(5,1,-2):
    print(i)

print( 5 // 2)

import math
print( math.floor(5/2) )
print( math.ceil(5/2) )
print( math.sqrt(16) )  

float("inf")
float("-inf")

# Arrays
arr = [1,2,3]

# Can be used as a stack
arr.pop()
arr.append(4)
arr.insert(1,7)
arr[0] = 0

n = 5
arr1 = [1] * n
print(arr[1:3]) # not including index 3

# loop through arrays

for i in range(len(arr)):
    print(arr[i])
# Without index
for n in arr:
    print(n)

# Looping through multiple arrays simultaneously with unpacking 
nums1 = [1,3,5]
nums2 = [2,4,6]
for n1,n2 in zip(nums1,nums2):
    print(n1,n2)
# Reverse
nums = [1,3,4]
nums.reverse()
nums.sort()

arr = ["bob","alice","jane"]
arr.sort()
print(arr)

arr.sort(key=lambda x: len(x))

arr = [i for i in range(5) ]
print(arr)

# Strings are similar to arrays
s = "abc"
s += "def"
print(s)


from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()
queue.appendleft(3)

mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)
print (1 in mySet)

mySet.remove(1)

#List to set
print(set([1,2,2,3,4,4]))

# Set comprehension
mySet = {i for i in range(5)}
print(mySet)

# Hash maps
myMap = {}
myMap["alice"] = 1
myMap["bob"] = 2
print(myMap)
print(len(myMap))
for key in myMap:
    print(key,myMap[key])

for val in myMap.values():
    print(val)  

import heapq
minHeap = []
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,1)
print(minHeap[0])

# Functions
def myFunc(x,y):
    return x+y  

# Nested functions have access to outer scope
