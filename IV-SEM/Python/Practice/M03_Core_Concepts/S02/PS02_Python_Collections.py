'''
s = {True,10,12.45,10,1,9+5j}
print(s,type(s))
print(s[3]) 

A = {1,2,3}
B = {3,4,5}
A.add(4)
B.update({6,7})
print(A,B)
A.pop()
print(A)
'''
#268. Missing Number
nums = [3,0,1]
def missingNumber(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums) 
    return total_sum - actual_sum
#349. Intersection of Two Arrays
nums1 = [1,2,2,1]
nums2 = [2,2]
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1.intersection(set2))
print(missingNumber(nums))
print(intersection(nums1, nums2))




