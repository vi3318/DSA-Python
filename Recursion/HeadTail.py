# Head Recursion is when the recursive call is made before any processing in the function.
# Tail Recursion is when the recursive call is the last operation in the function.
def head_recursion(n):
    if n == 0:
        return 
    print(head_recursion(n - 1))
    print(n)
    
def tail_recursion(n):
    if n == 0:
        return 
    print(n)
    print(tail_recursion(n - 1))

# Need to make recursion tree in every question

# TC O(n) for both head and tail recursion
# SC O(n) for both head and tail recursion due to call stack