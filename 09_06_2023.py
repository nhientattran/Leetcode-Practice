# 134. Gas Station

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

# Example 1:

# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.
# Example 2:

# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.

def canCompleteCircuit(gas, cost):
    gas_station = 0
    total_gas = 0
    current_gas = 0
    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]
        if current_gas < 0:
            current_gas = 0
            gas_station = i + 1
    if total_gas >= 0:
        return gas_station
    else:
        return -1

# 13. Roman to Integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def romanToInt(s):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    index = 0
    out = dic[s[0]]
    for i in range(1, len(s)):
        out += dic[s[i]]
        if dic[s[i]] > dic[s[index]]:
            out -= 2 * dic[s[index]]
        index += 1
    return out

