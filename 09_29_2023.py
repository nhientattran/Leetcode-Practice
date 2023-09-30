# A data analyst recently joined HackerRank as an intern.
# As an initial task, data for days is provided to the intern. Then, k updates are performed on the data, where each update is of the form [I, r]. This indicates that the subarray of data starting at index./ and ending at index r is negated. For
# example, if data = (1, 2, 3, 4] and the updates are (2, 4] then the data becomes data = [1, -2, -3, -4].
# Given the initial data and K updates, find the final data after all updates.
# Note: 1-based indexing is used.
# Example
# Consider n = 4, data = [1, 4, 5, 21, k - 2 and updates = [(2, 4], [1, 21).
# 1. After the first update, the data becomes data = 11, 4. 5. -21.
# 2. After the second update, the data becomes data = [-1, -4, 5, -2).
# The final data is /-1, 4, 5, -2).
# Function Description
# Complete the function getFinalData in the editor below.
# getfina/Data has the following parameters:
# int datan): the initial data
# int updates/kJ/2): updates in the form of [, r)
# Returns
# intin): the final data after all updates

def getFinalData(data, updates):
    for update in updates:
        for i in range(update[0]-1, update[1]):
            data[i] = -data[i]
    return data

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
 
def longestConsecutiveSequence(nums):
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

