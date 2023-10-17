# 168. Excel Sheet Column Title

# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"

def convertToTitle(columnNumber):
    out = ""
    while columnNumber > 0:
        columnNumber -= 1
        remainder = columnNumber % 26
        out = chr(65 + remainder) + out
        columnNumber = columnNumber // 26
    return out

# 944. Delete Columns to Make Sorted

# You are given an array of n strings strs, all of the same length.

# The strings can be arranged such that there is one on each line, making a grid.

# For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
# abc
# bce
# cae
# You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

# Return the number of columns that you will delete.

 

# Example 1:

# Input: strs = ["cba","daf","ghi"]
# Output: 1
# Explanation: The grid looks as follows:
#   cba
#   daf
#   ghi
# Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
# Example 2:

# Input: strs = ["a","b"]
# Output: 0
# Explanation: The grid looks as follows:
#   a
#   b
# Column 0 is the only column and is sorted, so you will not delete any columns.
# Example 3:

# Input: strs = ["zyx","wvu","tsr"]
# Output: 3
# Explanation: The grid looks as follows:
#   zyx
#   wvu
#   tsr
# All 3 columns are not sorted, so you will delete all 3.
 
def minDeletionSize(strs):
    out = 0
    for index in range(len(strs[0])):
        for i in range(1, len(strs)):
            if strs[i][index] < strs[i-1][index]:
                out += 1
                break
    return out


    