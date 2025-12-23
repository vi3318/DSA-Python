# freqMap = dict() / {}

freqMap={}
nums = [1,1,3,4,5,6,7,8,9]
for i in range (0, len(nums)):
    if nums[i] in freqMap:
        freqMap[nums[i]] +=1
    else:
        freqMap[nums[i]] = 1
x=1
print(freqMap[x])
# TC O(n)
# SC O(n)
hashMap = {}
for i in range(0, len(nums)):
    hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1

print(hashMap)

# TC O(n)
# SC O(n)