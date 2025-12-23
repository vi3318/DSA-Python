def recursionParameters(x, n):
    if n == 0:
        return 
    print(x)
    recursionParameters(x, n-1)

recursionParameters(15, 4)

# Always perform dry run to understand the flow of parameters