import random

# 380. Insert Delete GetRandom O(1)

# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

 

# Example 1:

# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

class RandomizedSet(object):

    def __init__(self):
        self.values = []
        self.val_index = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_index:
            return False
        self.val_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_index:
            last_val = self.values[-1]
            index = self.val_index[val]

            self.values[index] = last_val
            self.val_index[last_val] = index

            self.values.pop()
            del self.val_index[val]
            return True

        return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.values)

# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

def productExceptSelf(nums):
    output = []
    n = len(nums)
    left_product = [1]*n
    right_product = [1]*n
    for i in range(1,n):
        left_product[i] = left_product[i-1]*nums[i-1]
    for i in range(n-2, -1, -1):
        right_product[i] = right_product[i+1]*nums[i+1]
    for i in range(n):
        output.append(left_product[i]*right_product[i])
    return output




 
