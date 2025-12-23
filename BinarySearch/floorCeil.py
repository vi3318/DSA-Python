# floor and ceil in binary search 
def floor_ceil(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    floor = -1
    ceil = -1

    while low <= high:
        mid = (low + high) //2
        if nums[mid] == target:
            return nums[mid], nums[mid]
        elif nums[mid] < target:
            floor = nums[mid]
            low = mid + 1
        else:
            ceil = nums[mid]
            high = mid - 1
    return floor, ceil
nums = [1, 2, 4, 6, 8, 10]
target = 5
print(floor_ceil(nums, target))
# TC : O(log n)
# SC : O(1)