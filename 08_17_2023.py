# 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    dic = {}
    used = set()
    for i in range(len(s)):
        if s[i] not in dic:
            if t[i] in used:
                return False
            dic[s[i]] = t[i]
            used.add(t[i])
        elif s[i] in dic:
            if dic[s[i]] != t[i]:
                return False
    return True

# 290. Word Pattern

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

def wordPattern(pattern, s):
    s = s.split(' ')
    dic = {}
    used = set()
    if len(pattern) != len(s):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in dic:
            if s[i] in used:
                return False
            dic[pattern[i]] = s[i]
            used.add(s[i])
        else:
            if dic[pattern[i]] != s[i]:
                return False
    return True

# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(s, t):
    s_dic = {}
    t_dic = {}
    for word in s:
        if word not in s_dic:
            s_dic[word] = 1  
        else:
            s_dic[word] += 1
    for word in t:
        if word not in t_dic:
            t_dic[word] = 1
        else:
            t_dic[word] += 1
    return s_dic == t_dic

# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        sub = target - nums[i]
        if sub in dic:
            return [i, dic[sub]]
        if nums[i] not in dic:
            dic[nums[i]] = i
    
# 202. Happy Number

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def isHappy(n):
    nums = 0
    count = 0
    while count < 50:
        for num in str(n):
            nums += (int(num))**2
        n = nums
        if nums == 1:
            return True
        nums = 0
        count += 1
    return False

# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def containsNearbyDuplicate(nums, k):
    dic = {}
    for i, num in enumerate(nums):
        if num in dic and abs(i - dic[num]) <= k:
            return True
        dic[num] = i
    return False
