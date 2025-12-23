# Largest numnerber in an array

nums=[3, 5, 7, 2, 8, 6]
largest = nums[0]
# largest = float('-inf')  # Alternative way to initialize largest
n = len(nums)
for i in range(0,n):
    largest= max(largest, nums[i])

print("The largest number in the array is:", largest)

# TC : O(n)
# SC : O(1) 