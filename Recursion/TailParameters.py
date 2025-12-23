# printing 1 to 4 using tail recursion 
def tailRecursion(i,n):
    if i > n:
        return 
    print(i)
    tailRecursion(i+1, n)

tailRecursion(1, 4)

# printing 4 to 1 using head recursion
def headRecursion(i, n):
    if i > n:
        return
    headRecursion(i+1, n)
    print(i)

headRecursion(1, 4)

# printing 1 to 4 using head recursion 
def headRecursion2(i, n):
    if i > n:
        return
    headRecursion2(i, n-1)
    print(n)

# first func all headRecursion2(1,4) next call headRecursion2(1,3) and so on

headRecursion2(1, 4)