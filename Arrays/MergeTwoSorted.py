# Merge two sorted arrays

nums1 = [1,3,3,5,7]
nums2 = [2,4,6,8,8]

n = len(nums1)
m = len(nums2)
result = []
i,j=0
while i < n and j < m:
    if nums1[i] <= nums2[j]:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i+=1
    else:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j+=1

while i < n:
    if len(result) == 0 or result[-1] != nums1[i]:
        result.append(nums1[i])
    i+=1
while j < m:
    if len(result) == 0 or result[-1] != nums2[j]:
        result.append(nums2[j])
    j+=1

print(result)
# TC O(n + m)
# SC O(1) / O(n + m) if considering output array

