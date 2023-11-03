# 409. Longest Palindrome

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

def longestPalindrome(s):
    dic = {}
    for letter in s:
        if letter not in dic:
            dic[letter] = 1
        else:
            dic[letter] += 1
    longest_length = 0
    containt_odd = False
    for value in dic.values():
        if value % 2 == 0:
            longest_length += value
        else:
            longest_length += (value - 1)
            containt_odd = True
    if containt_odd:
        longest_length += 1
    return longest_length

# 412. Fizz Buzz

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

def fizzBuzz(n):
    out = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            out.append('FizzBuzz')
        elif num % 3 == 0:
            out.append('Fizz')
        elif num % 5 == 0:
            out.append('Buzz')
        else:
            out.append(str(num))
    return out
