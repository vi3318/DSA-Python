# remove duplicates from a sorted array

nums = [1,1,2,2,3,4,4,5]

n = len(nums)
frequencyMap = {}
for i in range(0,n):
    frequencyMap[nums[i]] = 0

j = 0
for k in frequencyMap:
    nums[j] = k
    j += 1

print("Number of unique elements:", j   )


# TC : O(2n)
# SC : O(n)