# Fibonacci series using recursion

def fibo(n):
    if n >= 1:
        return fibo(n-1) + fibo(n-2)
    elif n == 0:
        return 0
    else:
        return 1 
    
# TC = O(2^n)
# SC = O(n) due to function call stack