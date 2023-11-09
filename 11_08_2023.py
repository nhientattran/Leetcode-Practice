# 448. Find All Numbers Disappeared in an Array

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]

def findDisappearedNumbers(nums):
    for i in range(1, len(nums)):
        while nums[i] != nums[nums[i]-1]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    out = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            out.append(i + 1)
    return out

# 455. Assign Cookies

# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

 

# Example 1:

# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.
# Example 2:

# Input: g = [1,2], s = [1,2,3]
# Output: 2
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
# You have 3 cookies and their sizes are big enough to gratify all of the children, 
# You need to output 2.

def findContentChildren(g, s):
    out = 0
    g = sorted(g)
    s = sorted(s)

    i = len(g) - 1
    j = len(s) - 1
    
    while i >= 0 and j >= 0:
        if s[j] >= g[i]:
            out += 1
            i -= 1
            j -= 1
        else:
            i -= 1
    return out

