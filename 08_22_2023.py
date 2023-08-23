# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

def summaryRanges(nums):
    if not nums:
        return []
    out = []
    start = end = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == end + 1:
            end = nums[i]
        else:
            if end != start:
                out.append(f"{start}->{end}")
            else:
                out.append(str(start))
            start = end = nums[i]
    if start == end:
        out.append(f"{end}")
    else:
        out.append(f"{start}->{end}")
    return out

# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

def isPalindrome(x):
    if x < 0:
        return False
    return x == int(str(x)[::-1])

    
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

def plusOne(digits):
    digits_str = [str(num) for num in digits]
    numbers = int("".join(digits_str)) + 1
    return [int(num) for num in str(numbers)]

print(plusOne([9]))