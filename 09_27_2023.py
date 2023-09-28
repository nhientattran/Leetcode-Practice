# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

def topKFrequent(nums, k):
    dic = {}
    out = []    
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    max_freq = max(dic.values())
    while len(out) < k:
        for key, value in dic.items():
            if value == max_freq:
                out.append(key)
        max_freq -= 1
    return out

# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

def productExceptSelf(nums):
    output = []
    n = len(nums)
    left_product = [1]*n
    right_product = [1]*n   
    for i in range(1,n):
        left_product[i] = left_product[i-1]*nums[i-1]
    for i in range(n-2, -1, -1):
        right_product[i] = right_product[i+1]*nums[i+1]
    for i in range(n):
        output.append(left_product[i]*right_product[i])
    return output
