# 501. Find Mode in Binary Search Tree

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]

def findMode(root):
    if not root:
        return []

    stack = []
    modes = []
    prev_val = None
    current_freq = 0
    max_freq = 0

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if prev_val == root.val:
            current_freq += 1
        else:
            current_freq = 1

        if current_freq == max_freq:
            modes.append(root.val)
        elif current_freq > max_freq:
            max_freq = current_freq
            modes = [root.val]

        prev_val = root.val
        root = root.right

    return modes

# 504. Base 7

# Given an integer num, return a string of its base 7 representation.

 

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"

def convertToBase7(num):
    if num == 0:
        return "0"

    out = ''
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)

    while num > 0:
        out += str(num % 7)
        num //= 7

    if is_negative:
        out += '-'

    return out[::-1]

