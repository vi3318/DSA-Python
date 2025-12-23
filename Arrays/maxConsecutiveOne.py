# Max Consecutive Ones

# class Solution:
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     count = 0
    #     maxCount = 0
    #     for i in range(0,n):
    #         if nums[i] == 1:
    #             count+= 1
    #         else:
    #             maxCount = max(count, maxCount)
    #             count = 0

    #     return max(count, maxCount)

# TC O(N)
# SC O(1)
