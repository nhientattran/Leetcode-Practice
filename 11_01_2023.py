# 401. Binary Watch

# A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

# For example, the below binary watch reads "4:51".


# Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

# The hour must not contain a leading zero.

# For example, "01:00" is not valid. It should be "1:00".
# The minute must consist of two digits and may contain a leading zero.

# For example, "10:2" is not valid. It should be "10:02".
 

# Example 1:

# Input: turnedOn = 1
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
# Example 2:

# Input: turnedOn = 9
# Output: []
def readBinaryWatch(turnedOn):
    out = []
    for h in range(12):
        for m in range(60):
            if (bin(h) + bin(m)).count('1') == turnedOn:
                out.append('%d:%02d' % (h,m))
    return out

# 405. Convert a Number to Hexadecimal

# Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

# Note: You are not allowed to use any built-in library method to directly solve this problem.

 

# Example 1:

# Input: num = 26
# Output: "1a"
# Example 2:

# Input: num = -1
# Output: "ffffffff"

def toHex(num):
    if num == 0:
        return '0'
    
    dic = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    out = ''

    if num < 0:
        num += 2**32
    while num > 0:
        out += dic[(num % 16)]
        num = num // 16
    return out[::-1]