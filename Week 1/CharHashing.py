# Character hashing

s = "azxxya"
q = ["a", "b", "z", "x", "y", "d"]

hashed_list = [0] * 26
for char in s:
    ascii_value = ord(char)
    index = ascii_value - 97
    hashed_list[index] += 1

for char in q:
    ascii_value = ord(char)
    index = ascii_value - 97
    print(f"Frequency of {char}: {hashed_list[index]}")

# TC O(n + m) where n = len(s) and m = len(q)
# SC O(1) since the size of hashed_list is constant (26)