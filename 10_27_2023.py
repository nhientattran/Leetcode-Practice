# 349. Intersection of Two Arrays

# Companies
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 
def intersection(nums1, nums2):
    dic = {}
    out = []
    
    for num in set(nums1):
        dic[num] = 1
    
    for num in set(nums2):
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    
    for key, value in dic.items():
        if value > 1:
            out.append(key)
    
    return out

# 350. Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
 
def intersect(nums1, nums2):
    dic1 = {}
    dic2 = {}
    out = []

    for num in nums1:
        if num not in dic1:
            dic1[num] = 1
        else:
            dic1[num] += 1

    
    for num in nums2:
        if num not in dic2:
            dic2[num] = 1
        else:
            dic2[num] += 1
    
    for key, value in dic1.items():
        if key in dic2:
            if dic2[key] < value:
                for i in range(dic2[key]):
                    out.append(key)
            else:
                for i in range(value):
                    out.append(key)
        else:
            continue
    return out
