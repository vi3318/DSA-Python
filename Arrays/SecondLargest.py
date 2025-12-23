# Second largest number in an array

nums = [3, 5, 7, 2, 8, 6]

# Brute Force Approach
nums.sort()
print("second largest " , nums[-2])

# TC O(nlogn)
# SC O(1)
# Better Approach

largest = float('-inf')
secondLargest = float('-inf')

n = len(nums)
for i in range(0,n):
    largest = max(largest, nums[i])
for i in range(0,n):
    if nums[i] > secondLargest and nums[i] != largest:
        secondLargest = nums[i]

print("The second largest number in the array is:", secondLargest)

# TC : O(2n) = O(n)
# SC : O(1)
# Optimal Approach

largest1 = float('-inf')
secondLargest1 = float('-inf')
for i in range(0,n):
    if nums[i] > largest1:
        secondLargest1 = largest1
        largest1 = nums[i]
    elif nums[i] > secondLargest1 and nums[i] != largest1:
        secondLargest1 = nums[i]

print("The second largest number in the array is:", secondLargest1)

# TC : O(n)
# SC : O(1)