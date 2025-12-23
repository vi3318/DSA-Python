# Binary search 
def binary_search(nums, target):
    n = len(nums)
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1

        return -1

 
 # using recursion 
def binary_search_recursive(nums, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) //2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums , target, mid + 1, right)
    else:
        return binary_search_recursive(nums , target, left , mid-1)
    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(binary_search(nums, target))
print(binary_search_recursive(nums, target, 0, len(nums)-1))
# TC : O(log n) in powers of 2
# SC : O(1) for iterative , O(log n) for recursive due to call