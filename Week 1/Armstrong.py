# n  = 153
# noOfDigits = len(str(n))
# total = 0

def Armstrong(n):
    og = n
    noOfDigits = len(str(n))
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** noOfDigits
        n = n //10
    return total == og

print(Armstrong(153))

# TC O(log10(n))
# SC O(1)
