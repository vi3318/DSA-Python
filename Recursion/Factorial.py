# Factorial of a number using recursion
def Factorial(n):
    if n == 1 or n== 0:
        return 1
    return n * Factorial(n-1)

result = Factorial(4)
print(result)

# TC = O(n)
# SC = O(n) due to function call stack