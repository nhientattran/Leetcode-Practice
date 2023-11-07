# 434. Number of Segments in a String

# Given a string s, return the number of segments in the string.

# A segment is defined to be a contiguous sequence of non-space characters.

 

# Example 1:

# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
# Example 2:

# Input: s = "Hello"
# Output: 1

def countSegment(s):
    s = s.split(' ')
    count = 0
    for word in s:
        if len(word) != 0:
            count += 1
    return count


# 441. Arranging Coins

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.

def arrangeCoins(n):
    if n == 1:
        return 1
    row = 1
    count = 0
    while row <= n:
        n -= row
        row += 1
        count += 1
    return count

