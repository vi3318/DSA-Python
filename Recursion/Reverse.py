# Reverse an array using recursion 

# nums.reverse() method is not allowed
# nums.slice[::-1] method is not allowed

def ReverseArray(arr, left, right):
    if left >= right:
        return 
    arr[left], arr[right] = arr[right], arr[left]
    ReverseArray(arr, left + 1, right - 1)

nums = [1, 2, 3, 4, 5]
ReverseArray(nums, 0, len(nums) - 1)
print(nums)