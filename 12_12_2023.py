# 941. Valid Mountain Array

# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

# Example 1:

# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true

def validMountainArray(arr):
    if len(arr) < 3:
        return False
    for i in range(1, len(arr)):
        if arr[i] != max(arr):
            if arr[i] <= arr[i-1]:
                return False
        else:
            if arr[i] <= arr[i-1]:
                return False
            if i == len(arr) - 1:
                return False
            for j in range(i, len(arr)-1):
                if arr[j] <= arr[j+1]:
                    return False
            break
    return True

# 953. Verifying an Alien Dictionary

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

def isAlienSorted(words, order):
    alien_dict = {c: i for i, c in enumerate(order)}

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for c1, c2 in zip(word1, word2):
            if alien_dict[c1] < alien_dict[c2]:
                break
            elif alien_dict[c1] > alien_dict[c2]:
                return False
        else:
            if len(word1) > len(word2):
                return False

    return True
