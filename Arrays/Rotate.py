# Brute Force Approach

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for _ in range(0,k):
            e = nums.pop()
            nums.insert(0,e)
 
# 1 2 3 4 
# 2
# 3 4 1 2 
# TC O(r*n)
# r is number of rotations
# n is number of elements in the array
# SC O(1)

# Better solution using slicing
# k = k%n
# nums[:] = nums[n-k:] + nums[:n-k]
# TC O(n) for slicing Or O(n-k) 
# SC O(1)

# Optimal solution using Reversal Algorithm
# TC O(k/2) + O((n-k)/2) + O(n/2) = O(n)
