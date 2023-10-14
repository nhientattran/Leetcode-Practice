# 118. Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

def generate(numRows):
    out = []
    for num in range(1, numRows+1): 
        out.append([1]*num) 
    
    if numRows <= 2:
        return out
    
    for i in range(2, numRows):
        for j in range(1, len(out[i-1])):
            out[i][j] = out[i-1][j-1] + out[i-1][j]
    return out 
    
# 119. Pascal's Triangle II

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    
    prev_row = [1]
    for i in range(1, rowIndex+1): 
        cur_row = [1]
        for j in range(1, len(prev_row)):
            cur_row.append(prev_row[j-1] + prev_row[j])
        cur_row.append(1)
        prev_row = cur_row
    return cur_row

print(getRow(3))

