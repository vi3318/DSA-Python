num = 1234
result = 0

def palindrome(num):
    og = num
    result = 0
    while num > 0:
        lastdigit = num % 10
        result = (result * 10) + lastdigit
        num = num // 10

    return result == og

print(palindrome(1232))

# TC O(log10(n))
# SC O(1)

