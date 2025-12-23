# Brute Force Approach to find factors of a number

def Printfactors(n):
    result = []
    for i in range(1,n+1):
        if n % i == 0:
            result.append(i)
    return result

print(Printfactors(12))


# TC O(n)
# SC O(k) using extra space for result list where k is number of factors

# Better Approach to find factors of a number
def Printfactors_better(n):
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)  # n is also a factor
    return result

print(Printfactors_better(12))

from math import sqrt
# Optimal solution to find factors of a number
def Printfactors_optimal(n):
    result = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            if n// i != i:
                result.append(n // i)
    result.sort()
    return result

print(Printfactors_optimal(12))

# TC O(sqrt(n)) with sorting it will be O(sqrt(n) + O(log(sqrt(n))))
# SC O(k) using extra space for result list where k is number of factors
      