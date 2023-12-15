# 976. Largest Perimeter Triangle

# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
# Example 2:

# Input: nums = [1,2,1,10]
# Output: 0
# Explanation: 
# You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

def largestPerimeter(nums):
    nums = sorted(nums, reverse=True)
    max_perimeter = 0
    for i in range(len(nums)-2):
        if nums[i] < nums[i+1] + nums[i+2]:
            max_perimeter = max(max_perimeter, nums[i]+ nums[i+1] + nums[i+2])
    return max_perimeter

# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    index = n - 1  

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square >= right_square:
            result[index] = left_square
            left += 1
        else:
            result[index] = right_square
            right -= 1

        index -= 1

    return result

print(bool('abc'))