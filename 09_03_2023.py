# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

def addBinary(a, b):
    output = bin(int(a,2) + int(b,2))
    return output[2:]

# 2103. Rings and Rods

# There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.

# You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:

# The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
# The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
# For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.

# Return the number of rods that have all three colors of rings on them.

def countPoints(rings):
    dic = {}
    count = 0
    for i in range(1, len(rings), 2):
        if rings[i] not in dic:
            dic[rings[i]] = rings[i-1]
        else:
            dic[rings[i]] += rings[i-1]
    for value in dic.values():
        if 'R' in value and 'G' in value and 'B' in value:
            count += 1
    return count

# 2744. Find Maximum Number of String Pairs

# You are given a 0-indexed array words consisting of distinct strings.

# The string words[i] can be paired with the string words[j] if:

# The string words[i] is equal to the reversed string of words[j].
# 0 <= i < j < words.length.
# Return the maximum number of pairs that can be formed from the array words.

# Note that each string can belong in at most one pair.

# Example 1:

# Input: words = ["cd","ac","dc","ca","zz"]
# Output: 2
# Explanation: In this example, we can form 2 pair of strings in the following way:
# - We pair the 0th string with the 2nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
# - We pair the 1st string with the 3rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
# It can be proven that 2 is the maximum number of pairs that can be formed.
# Example 2:

# Input: words = ["ab","ba","cc"]
# Output: 1
# Explanation: In this example, we can form 1 pair of strings in the following way:
# - We pair the 0th string with the 1st string, as the reversed string of words[1] is "ab" and is equal to words[0].
# It can be proven that 1 is the maximum number of pairs that can be formed.
# Example 3:

# Input: words = ["aa","ab"]
# Output: 0
# Explanation: In this example, we are unable to form any pair of strings.

def maximumNumberOfStringPairs(words):
    count = 0
    j = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] == words[j][::-1]:
                count += 1
                break
    return count
 
# 1844. Replace All Digits with Characters

# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

# Example 1:

# Input: s = "a1c1e1"
# Output: "abcdef"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('c',1) = 'd'
# - s[5] -> shift('e',1) = 'f'
# Example 2:

# Input: s = "a1b2c3d4e"
# Output: "abbdcfdhe"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('b',2) = 'd'
# - s[5] -> shift('c',3) = 'f'
# - s[7] -> shift('d',4) = 'h'

def replaceDigits(s):
    output = ''
    alphabet = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}
    words_dic = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    
    for i in range(1, len(s), 2):
        output += s[i-1] + alphabet[words_dic[s[i-1]]+int(s[i])]
    
    if len(s) % 2 == 0:
        return output
    else:
        return output + s[-1]

