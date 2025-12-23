# Right Rotate an Array by 1 place
nums = [1, 2, 3, 4, 5]
n = len(nums)

# Make a copy at the same address and rotate in place
nums[:] = nums[-1] + nums[0:n-1]

# TC : O(n-1) for slicing 
# SC : O(1)

# Without slicing
temp = nums[n-1]

for i in range(n-2, -1,-1):
    nums[i+1] = nums[i]

nums[0] = temp

# TC : O(n-1)
# SC : O(1)

