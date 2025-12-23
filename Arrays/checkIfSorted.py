nums = [3, 5, 7, 2, 8, 6]

def check_if_sorted(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False
    return True
print(check_if_sorted(nums))

# TC : O(n)
# SC : O(1)