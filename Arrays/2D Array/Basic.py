# 2D matrix
nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

rows = len(nums)
cols = len(nums[0])

for i in range(0,rows):
    for j in range(0,cols):
        print(nums[i][j], end=" ")
    print()

# print upper triangle
for i in range(0,rows):
    for j in range(0,cols):
        if j >= i:
            print(nums[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
 
# Transpose
result = [[0] * rows for _ in range(cols)]

for i in range(0,rows):
    for j in range(0,cols):
        result[j][i] = nums[i][j]