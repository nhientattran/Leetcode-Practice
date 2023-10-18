import math
# 231. Power of Two

# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false

def isPowerOfTwo(n):
    if n <= 0:
        return False
    out_num = math.log(n, 2)
    tolerance = 1e-10
    if abs(int(out_num) - out_num) > tolerance:
        return False
    else:
        return True
    
# 258. Add Digits

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# Example 2:

# Input: num = 0
# Output: 0

def addDigits(num):
    while len(str(num)) != 1:
        num = sum(int(n) for n in str(num))
    return num

