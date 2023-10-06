# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

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
