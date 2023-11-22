# 506. Relative Ranks

# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

 
import math

# Example 1:

# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# Example 2:

# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

def findRelativeRanks(score):
    sorted_score = sorted(score, reverse=True)
    dic = {}
    out = []
    for i in range(len(sorted_score)):
        if i == 0:
            dic[sorted_score[i]] = 'Gold Medal'
        elif i == 1:
            dic[sorted_score[i]] = 'Silver Medal'
        elif i == 2:
            dic[sorted_score[i]] = 'Bronze Medal'
        else:
            dic[sorted_score[i]] = str(i + 1)
    for num in score:
        out.append(dic[num])
    return out

# 507. Perfect Number

# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.

 

# Example 1:

# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
# Example 2:

# Input: num = 7
# Output: false

def checkPerfectNumber(num):
    if num <= 1:
        return False
    out = 1
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            out += i
            if i != num // i:
                out += num // i
    return num == out

 