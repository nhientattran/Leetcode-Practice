# 459. Repeated Substring Pattern

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


def repeatedSubstringPattern(s):
    for i in range(1, len(s)):
        if len(s) % i == 0:
            sub_s = s[:i]
            if sub_s * (len(s) // i) == s:
                return True
    return False


# 461. Hamming Distance

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

 

# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:

# Input: x = 3, y = 1
# Output: 1

def hammingDistance(x, y):
    xor_result = x ^ y
    hamming_distance = 0
    while xor_result:
        hamming_distance += xor_result & 1
        xor_result >>= 1
    return hamming_distance



 
