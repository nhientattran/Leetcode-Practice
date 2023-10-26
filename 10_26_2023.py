# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 
def reserveString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

def reserveVowels(s):
    vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    s_2 = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s_2[left] in vowels and s_2[right] in vowels:
            s_2[left], s_2[right] = s_2[right], s_2[left]
            left += 1
            right -= 1
        elif s_2[left] in vowels and s_2[right] not in vowels:
            right -= 1
        elif s_2[right] in vowels and s_2[left] not in vowels:
            left += 1
        else:
            left += 1
            right -= 1
    return ''.join(s_2)

