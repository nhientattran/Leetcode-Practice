# 414. Third Maximum Number

# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

def thirdMax(nums):
    first_max = second_max = third_max = float('-inf')
    
    for num in nums:
        if num > first_max:
            third_max = second_max
            second_max = first_max
            first_max = num
        elif first_max > num > second_max:
            third_max = second_max
            second_max = num
        elif second_max > num > third_max:
            third_max = num
    
    if third_max == float('-inf'):
        return first_max
    else:
        return third_max

# 415. Add Strings

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"

def addStrings(num1, num2):
    i, j, carry = len(num1) - 1, len(num2) - 1, 0
    out = []

    while i >= 0 or j >= 0 or carry:
        x1 = int(num1[i]) if i >= 0 else 0
        x2 = int(num2[j]) if j >= 0 else 0

        total = x1 + x2 + carry
        carry = total // 10
        out.append(str(total % 10))

        i -= 1
        j -= 1
    
    return ''.join(out[::-1])