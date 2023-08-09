# Two Sum:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        sub = target - nums[i]
        if sub not in dic:
            dic[nums[i]] = i
        else:
            return [dic[sub], i]
        

# 1108. Defanging an IP Address

# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

def defangIPaddr(address):
    out = address.replace('.', '[.]')
    return out

# print(defangIPaddr("1.1.1.1"))