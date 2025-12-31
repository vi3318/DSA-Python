
arr = [1, 2, 3]
result = []

def func(index, subset):
    if index >= len(arr):
        result.append(subset.copy())
        return
    subset.append(arr[index])
    func(index +1 , subset)
    subset.pop()
    func(index + 1, subset)