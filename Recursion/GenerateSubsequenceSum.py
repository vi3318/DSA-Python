result=[]
nums = [1,2,3]
k=3
Sum =0
total=0

def backtrack(index,total,subset):
    if total == k:
        result.append(subset.copy())
        return
    elif total > k:
        return
    
    if index >= len(nums):
        return 
    subset.append(nums[index])
    Sum = total + nums[index]
    backtrack(index+1, Sum, subset)
    e = subset.pop()
    Sum -= e

    backtrack(index + 1, Sum, subset)

# TC : O(2^n)
# SC : O(n)
