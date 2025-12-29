# Convert a number to binary

def convert_to_binary(n):
    result = ""
    while n > 0:
        if n % 2 == 1:
            result += "1"
        else:
            result += "0"
        n = n // 2
    result = result[::-1]
    return result

# Example usage
number = 3
binary_representation = convert_to_binary(number)
print(f"Binary representation of {number} is {binary_representation}")
# TC : O(log n)
# SC : O(log n)

def convert_to_decimal(binary_str):
    decimalNumber = 0
    power = 0
    index = len(binary_str) - 1
    while index >= 0: 
        num = int(binary_str[index]) * (2 ** power)
        decimalNumber += num
        power += 1
        index -= 1
    return decimalNumber

# Example usage
binary_string = "11"
decimal_representation = convert_to_decimal(binary_string)
print(f"Decimal representation of {binary_string} is {decimal_representation}")
# TC : O(len)
# SC : O(1)
         
         
# 1 s complement and 2 s complement of a number

# Swapping two numbers using XOR
a = 10
b = 5
print(f"Before swapping: a = {a}, b = {b}")
a = a ^ b
b = (a ^ b ) 
a = (a ^ b) 
print(f"After swapping: a = {a}, b = {b}")

# Check if ith bit is set or not
n = 13
i = 2
# using left shift
if (n & (1 << i)) != 0:
    print(f"{i}th bit is set")
else:
    print(f"{i}th bit is not set")

# using right shift 
if (n >> i) & 1 != 0:
    print(f"{i}th bit is set")
else:
    print(f"{i}th bit is not set")
# Set the ith bit
n =9
i = 2

n | (i << 2)
print(f"Number after setting {i}th bit is {n}")
n & ~(1 << i)
print(f"Number after clearing {i}th bit is {n}")
