# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence(s, t):
    if s == '':
        return True
    k = 0
    count = 0
    for char in t:
        if char == s[k]:
            k += 1
            count += 1
        if count == len(s):
            return True
    return False

# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

def canConstruct(ransomNote, magazine):
    ran_dic = {}
    mag_dic = {}
    for letter in ransomNote:
        if letter not in ran_dic:
            ran_dic[letter] = 1
        else:
            ran_dic[letter] += 1
    for letter in magazine:
        if letter not in mag_dic:
            mag_dic[letter] = 1
        else:
            mag_dic[letter] += 1
    for letter in ransomNote:
        if letter not in mag_dic or ran_dic[letter] > mag_dic[letter]:
            return False
    return True

# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']
    pair = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in s:
        if char in open_list:
            stack.append(char)
        elif char in close_list:
            if not stack:
                return False
            last_bracket = stack.pop()
            if pair[last_bracket] != char:
                return False
    return not stack
