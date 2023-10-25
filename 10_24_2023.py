# 283. Move Zeroes

# Companies
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

def moveZeros(nums):
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1

# 292. Nim Game

# You are playing the following Nim Game with your friend:

# Initially, there is a heap of stones on the table.
# You and your friend will alternate taking turns, and you go first.
# On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
# The one who removes the last stone is the winner.
# Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

 

# Example 1:

# Input: n = 4
# Output: false
# Explanation: These are the possible outcomes:
# 1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
# 2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
# 3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
# In all outcomes, your friend wins.
# Example 2:

# Input: n = 1
# Output: true
# Example 3:

# Input: n = 2
# Output: true
 

# Constraints:

# 1 <= n <= 231 - 1

def canWinNim(n):
    rate = n % 4
    return rate == 0
        