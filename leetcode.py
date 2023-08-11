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

# 771. Jewels and Stones
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

def numJewelsInStones(jewels, stones):
    return sum(1 for stone in stones if stone in jewels)

# 2011. Final Value of Variable After Performing Operations
# There is a programming language with only four operations and one variable X:
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

def finalValueAfterOperation(operations):
    dic = {'++X': 1, 'X++': 1, '--X': -1, 'X--': -1}
    return sum(dic[ope] for ope in operations)


# Goal Parser Interpretation
# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.

def interpret(command):
    out = ''
    for i in range(len(command)):
        if command[i] == '(' and command[i+1] == ')':
            out += 'o'
        elif command[i] == '(' and command[i+1] != ')':
            out += 'al'
        elif command[i] == 'G':
            out += 'G'
    return out

# 2114. Maximum Number of Words Found in Sentences
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.

def mostWordsFound(sentence):
    max_count = 0
    for sen in sentence:
        if len(sen.split(" ")) > max_count:
            max_count = len(sen.split(" "))
    return max_count

print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))