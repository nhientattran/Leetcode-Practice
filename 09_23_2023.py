# 69. Sqrt(x)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

def mySqrt(x):
    if x < 1:
        return 0
    num = 1
    sqrt = num * num

    while sqrt < x:
        num += 1
        sqrt = num * num

    if sqrt > x:
        return num - 1
    else:
        return num

# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

def reverse(x):
    int_max = 2**31 - 1
    int_min = -2**31

    reversed_x = int(str(abs(x))[::-1])
    if x < 0:
        reversed_x = 0 - reversed_x
    if reversed_x < int_min or reversed_x > int_max:
        return 0
    return reversed_x

