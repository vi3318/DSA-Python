# move zero
nums = [0,1,2,4]

n = len(nums)
# Brute force
for i in range(0,n+1):
    if i not in nums:
        print(i) 
# TC O(N2)
# SC O(1)

        # Better
freq= {}
for i in range(0,n+1):
    freq[i] = 0

for num in nums:
    freq[num] = 1

for k,v in freq.items():
    if v == 0:
        print(k)  

# TC O(3N)
# SC O(N)

# Optimal
# (n*(n+1))//2 - sum(nums)
# TC O(N)
# SC O(1)