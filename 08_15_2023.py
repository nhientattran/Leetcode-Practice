# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement(nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    for key, value in dic.items():
        if value > len(nums)/2:
            return key
        
# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    out = 0
    num = 0
    for i in range(len(prices)-1):
        num = max(prices[(i+1):len(prices)]) - prices[i]
        if num > out:
            out = num
    return out

def maxProfit2(prices):
    min_ = prices[0]
    profit = [0]
    for price in prices:
        if price < min_:
            min_ = price
        if price > min_:
            profit.append(price - min_)
    return max(profit)

# 58. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

def lengthOfLastWord(s):
    s = s.strip().split(' ')
    return len(str(s[-1]))

# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    k = 0
    if not strs:
        return ""
    min_len = min(len(word) for word in strs)
    while k < min_len:
        letter = strs[0][k]
        for word in strs:
            if word[k] != letter:
                return strs[0][:k]
        k += 1
    return strs[0][:k]

# 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i:i+len(needle)] == needle:
                return i




