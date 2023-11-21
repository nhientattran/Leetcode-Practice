# 500. Keyboard Row

# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

 

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:

# Input: words = ["omk"]
# Output: []
# Example 3:

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]

def findWords(words):
    f_round = set("qwertyuiop")
    s_round = set("asdfghjkl")
    t_round = set("zxcvbnm")
    out = []
    for word in words:
        words_list = set(word.lower())
        if words_list.issubset(f_round) or words_list.issubset(s_round) or words_list.issubset(t_round):
            out.append(word)
    return out


