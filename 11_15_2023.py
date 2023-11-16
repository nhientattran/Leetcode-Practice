# 482. License Key Formatting

# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

# Return the reformatted license key.

 

# Example 1:

# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.
# Example 2:

# Input: s = "2-5g-3-J", k = 2
# Output: "2-5G-3J"
# Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

def licenseKeyFormatting(s, k):
    s = s.replace('-', '').upper()
    first_len = len(s) % k
    out = s[:first_len]

    if not s:
        return ''
    
    for i in range(first_len, len(s), k):
        out += '-' + s[i:i+k]
    

    if out[0] == '-':
        return out[1:]
    return out


# 485. Max Consecutive Ones

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

def findMaxConsecutiveOnes(nums):
    consecutive_list = []
    count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            consecutive_list.append(count)
            count = 0
    consecutive_list.append(count)
    return max(consecutive_list)
