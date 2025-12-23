# linear search 
arr = [23, 45, 12, 67, 34, 89, 90]
target = 67
n = len(arr)
for i in range(0,n):
    if arr[i] == target:
        print("Element found at index:", i)
        break

print("Element not found in the array")