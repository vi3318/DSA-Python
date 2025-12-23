s = "racecar"

n = len(s)
left = 0
right = n - 1

while left < right:
    if s[left] != s[right]:
        print("Not a palindrome")
        break
    left += 1
    right -= 1

print("Palindrome")
# TC = O(n/2) = O(n)
# SC = O(1)

# using recursion
def isPalindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return isPalindrome(s, left +1, right-1)


# TC = O(n)
# SC = O(n) due to function call stack
print(isPalindrome("wow",0,2))