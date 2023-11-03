# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1

def firstUniqChar(s):
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = i
        else:
            dic[s[i]] = -1
    for value in dic.values():
        if value != -1:
            return value
    return -1

# 389. Find the Difference

# You are given two strings s and t.

# String t is generated by random shuffling string s and then add one more letter at a random position.

# Return the letter that was added to t.

 

# Example 1:

# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.
# Example 2:

# Input: s = "", t = "y"
# Output: "y"

def findTheDifference(s, t):
    dic = {}
    for word in s:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    for word in t:
        if word in dic and dic[word] > 0:
            dic[word] -= 1
        else:
            return word


 