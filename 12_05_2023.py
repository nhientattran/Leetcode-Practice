# 728. Self Dividing Numbers
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

# Example 1:
# Input: left = 1, right = 22# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]# Example 2:
# Input: left = 47, right = 85# Output: [48,55,66,77]
def selfDividingNumber(left, right):
    out = []
    count = 0
    for num in range(left, right + 1):
        if '0' in str(num):
            continue
        for i in range(len(str(num))):
            if num % int(str(num)[i]) == 0:
                count += 1
            else:
                break
            if count == len(str(num)):
                out.append(num)
                count = 0
    return out

# 724. Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

# Example 1:
# Input: nums = [1,7,3,6,5,6]# Output: 3# Explanation:# The pivot index is 3.# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11# Right sum = nums[4] + nums[5] = 5 + 6 = 11# Example 2:
# Input: nums = [1,2,3]# Output: -1# Explanation:# There is no index that satisfies the conditions in the problem statement.# Example 3:
# Input: nums = [2,1,-1]# Output: 0# Explanation:# The pivot index is 0.# Left sum = 0 (no elements to the left of index 0)# Right sum = nums[1] + nums[2] = 1 + -1 = 0

def pivotIndex(nums):
    total = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == total - left_sum - num:
            return i
        left_sum += num
    return -1