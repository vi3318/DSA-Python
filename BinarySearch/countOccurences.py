# Count the occurences of an element in a sorted array using binary search

# Brute force
def count_occurences_brute(nums, target):
    first = -1
    last = -1
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    if first == -1:
        return 0
    return last - first + 1

# TC : O(n)
# SC : O(1)

def lower_bound(nums, target):
    lb = -1
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb


def upper_bound(nums, target):
    ub = len(nums)-1
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub


# Example usage
nums = [1, 2, 2, 2, 3, 4, 5]
target = 2

lb = lower_bound(nums, target)
ub = upper_bound(nums, target)

if lb == -1:
    print(0)


    print(ub - lb)

# TC : O(log n)
# SC : O(1)


