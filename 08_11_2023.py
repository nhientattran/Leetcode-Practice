# 1221. Split a String in Balanced Strings
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

def balancedStringSplit(s):
    count = 0
    out_count = 0
    for char in s:
        count += 1 if char == 'R' else -1
        if count == 0:
            out_count += 1
    return out_count

# 1528. Shuffle String
# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

def restoreString(s, indices):
    dic = {}
    out = ''
    for i in range(len(s)):
        dic[indices[i]] = s[i]
    for i in range(len(indices)):
        out += dic[i]
    return out

# 1773. Count Items Matching a Rule
# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
# The ith item is said to match the rule if one of the following is true:
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

def countMatches(items, ruleKey, ruleValue):
    dic = {'type': 0, 'color': 1, 'name': 2}
    count = 0
    for item in items:
        if item[dic[ruleKey]] == ruleValue:
            count += 1
    return count

print(countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", 'phone'))