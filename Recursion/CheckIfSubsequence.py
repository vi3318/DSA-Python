result=[]
nums = [1,2,3]
k=3
Sum =0
total=0


def check(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return True
    elif total > k:
        return False
    if index >= len(nums):
        return False
    subset.append(nums[index])
    Sum = total + nums[index]
    pick = check(index+1, Sum, subset)
    if pick:
        return True
    e = subset.pop()
    Sum -= e
    notPick = check(index + 1, Sum, subset)
    return notPick

