
# 575. Distribute Candies

# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

# Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

 

# Example 1:

# Input: candyType = [1,1,2,2,3,3]
# Output: 3
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
# Example 2:

# Input: candyType = [1,1,2,3]
# Output: 2
# Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.
# Example 3:

# Input: candyType = [6,6,6,6]
# Output: 1
# Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.

def distributeCandies(candyType):
    candy = set(candyType)
    n = len(candyType) / 2
    if n > len(candy):
        return len(candy)
    else:
        return n


# 594. Longest Harmonious Subsequence

# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 2
# Example 3:

# Input: nums = [1,1,1,1]
# Output: 0

def findLHS(nums):
    dic = {}
    out = 0
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    for num in dic:
        if num + 1 in dic:
            length = dic[num] + dic[num + 1]
            out = max(out, length)
    return out
