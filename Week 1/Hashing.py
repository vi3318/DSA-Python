n = [1,1,3,4,5,6,7,8,9]
m = [100, 10 , 19, 10 , 9 , 9 , 10]

# Brute Force Approach
for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1
    print(f"Frequency of {num} is {count}")

# TLE

hashed_list = [0] * 11
for num in n:
    hashed_list[num] += 1

for x in m:
    if x < 1 or x > 10:
        print(0)
    else:
        print(hashed_list[x])

# TC : O(N + M)
# SC : O(1)

# Optimal Approach using Dictionary
frequency_map = {}
for num in n:
    frequency_map[num] = frequency_map.get(num, 0) + 1

for x in m:
    if x in frequency_map:
        print(frequency_map[x])
    else:
        print(0)