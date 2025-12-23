# Parameterized recursion for sum of 1 to n 
def ParameterizedSum(sum,i,n):
    if i > n:
        print(sum)
        return 
    ParameterizedSum(sum + i, i+1, n)

ParameterizedSum(0, 1, 4)

# Functional Recursion 
def FunctionalSum(n):
    if n ==1:
        return 1
    return n + FunctionalSum(n-1)

result = FunctionalSum(4)
print(result)

# TC = O(n)
# SC = O(n) due to function call stack