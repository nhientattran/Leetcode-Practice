# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

def threeSum(nums):
    nums = sorted(nums)
    out = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i + 1, len(nums) - 1

        while left < right:
            total_sum = nums[i] + nums[left] + nums[right]
            if total_sum == 0:
                out.append([nums[i], nums[left], nums[right]])
                while nums[left] == nums[left + 1]:
                    left += 1
                while nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total_sum < 0:
                left += 1
            else:
                right -= 1
    return out

# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest 
# substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
    if not s:
        return 0
    left = 0
    count = 0
    index_dic = {}
    for right in range(len(s)):
        if s[right] in index_dic and index_dic[s[right]] >= left:
            left = index_dic[s[right]] + 1

        index_dic[s[right]] = right
        count = max(count, right - left + 1)
    return count
            
            
