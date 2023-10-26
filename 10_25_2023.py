import math
# 326. Power of Three

# Companies
# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).

def isPowerOfThree(n):
    if n <= 0:
        return False
    
    while n % 3 == 0:
        n /= 3
    
    return n == 1

# 342. Power of Four

# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 

# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true
 

# Constraints:

# -231 <= n <= 231 - 1

def isPowerOfFour(n):
    if n <= 0:
        return False
    
    while n % 4 == 0:
        n /= 4
    
    return n == 1