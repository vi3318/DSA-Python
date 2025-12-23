# Selection Sort Implementation

def selectionSort(nums):
    n = len(nums)
    for i in range(0,n):
        min_index = i
        for j in range(i+1, n):
            if(nums[j] < nums[min_index]):
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

# O(n(n-1)/2) -> O(n^2)
# TC -> O(n^2)
# SC -> O(1)