# 1232. Check If It Is a Straight Line

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Example 1:



# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# Example 2:



# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: 

print(sorted([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))

def checkStraightLine(coordinates):
    if len(coordinates) <= 2:
        return True
    
    for i in range(2, len(coordinates)):
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x3, y3 = coordinates[i]

        if (y3 - y1) * (x2 - x1) != (y2 - y1) * (x3 - x1):
            return False
    
    return True

# 1295. Find Numbers with Even Number of Digits

# Given an array nums of integers, return how many of them contain an even number of digits.

 

# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.

def findNumbers(nums):
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    return count
 