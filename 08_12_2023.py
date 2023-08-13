import string 

# 2194. Cells in a Range on an Excel Sheet
# A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:

# <col> denotes the column number c of the cell. It is represented by alphabetical letters.
# For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
# <row> is the row number r of the cell. The rth row is represented by the integer r.
# You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the column c1, <row1> represents the row r1, <col2> represents the column c2, and <row2> represents the row r2, such that r1 <= r2 and c1 <= c2.

# Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2. The cells should be represented as strings in the format mentioned above and be sorted in non-decreasing order first by columns and then by rows.

def cellsInRange(s):
    words_dic = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    words = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    col = words[words_dic[s[0]] : words_dic[s[3]] + 1]
    row = range(int(s[1]), int(s[4]) + 1)
    out = []
    for word in col:
        for num in row:
            out.append(f"{word}{num}")
    return out

# 518. Coin Change II

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]

# 1662. Check If Two String Arrays are Equivalent

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

def arrayStringAreEqual(word1, word2):
    return "".join(word1) == "".join(word2)

# 2325. Decode the Message
# You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.

def decodeMessage(key, message):
    key = key.replace(' ', '')
    dic = {}
    alphabet = list(string.ascii_lowercase)
    final_key = ''
    output = ""
    for word in key:
        if word not in final_key:
            final_key += word
    for i in range(len(final_key)):
        dic[final_key[i]] = alphabet[i]
    for word in message:
        if word != ' ':
            output += dic[word]
        elif word == ' ':
            output += ' '
    return output
    

