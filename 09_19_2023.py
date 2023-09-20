# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

def addBinary(a, b):
    out = int(a, 2) + int(b, 2)
    return bin(out)[2:]
    

# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 
# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 
def longestConsecutive(nums):
    num_set = set(nums)
    long_sequence = 0
    short_sequence = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            short_sequence = 1

            while current_num + 1 in num_set:
                current_num += 1
                short_sequence += 1
            
            long_sequence = max(short_sequence, long_sequence)
    return long_sequence

