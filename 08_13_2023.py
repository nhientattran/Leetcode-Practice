import string

# 1816. Truncate Sentence

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.

def truncateSentence(s, k):
    return ' '.join(s.split(' ')[0:k])

# 1859. Sorting the Sentence

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

def sortSentence(s):
    s2 = s.split(' ')
    s3 = []
    i = 1
    while i <= len(s2):
        for word in s2:
            if str(i) in word:
                s3.append(word[0:-1])
                i += 1
    return ' '.join(s3)

# 1832. Check if the Sentence Is Pangram

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

def checkIfPangram(sentence):
    alphabet = list(string.ascii_lowercase)
    word = []
    for char in sentence:
        if char not in word:
            word.append(char)
    return sorted(word) == alphabet

# 804. Unique Morse Code Words

# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

def uniqueMorseRepresentations(words):
    dic = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e':".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-",'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."}
    morse = ''
    morse_list = []
    for word in words:
        for letter in word:
            morse += dic[letter]
        morse_list.append(morse)
        morse = ''
    return len(set(morse_list))

# 709. To Lower Case

# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

def toLowerCase(s):
    return s.lower()
    
# 1684. Count the Number of Consistent Strings

# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.

def countConsistentStrings(allowed, words):
    count = len(words)
    for word in words:
        for letter in word:
            if letter not in allowed:
                count -= 1
                break
    return count

# 2810. Faulty Keyboard

# Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have written. Typing other characters works as expected.

# You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.

# Return the final string that will be present on your laptop screen.

def finalString(s):
    out = ''
    for letter in s:
        if letter != 'i':
            out += letter
        else:
            out = out[::-1]
    return out

# 2697. Lexicographically Smallest Palindrome

# You are given a string s consisting of lowercase English letters, and you are allowed to perform operations on it. In one operation, you can replace a character in s with another lowercase English letter.

# Your task is to make s a palindrome with the minimum number of operations possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.

# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

# Return the resulting palindrome string.

def makeSmallestPalindrome(s):
    alphabet = list(string.ascii_lowercase)
    s = list(s)
    for i in range(len(s)):
        if s[i] != s[-1-i]:
            if alphabet.index(s[i]) > alphabet.index(s[-1-i]):
                s[i] = s[-1-i]
            else:
                s[-1-i] = s[i]
    return ''.join(s)

# 557. Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
 
def reverseWords(s):
    s = s.split(' ')
    out = []
    for word in s:
        out.append(word[::-1])
    return ' '.join(out)

# 1614. Maximum Nesting Depth of the Parentheses

# A string is a valid parentheses string (denoted VPS) if it meets one of the following:

# It is an empty string "", or a single character not equal to "(" or ")",
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:

# depth("") = 0
# depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

# Given a VPS represented as string s, return the nesting depth of s.

def maxDepth(s):
    count_list = []
    count = 0
    if s == '' or '(' not in s:
        return 0
    for letter in s:
        if letter == '(':
            count += 1
        elif letter == ')':
            count_list.append(count)
            count -= 1
    return max(count_list)

# 2315. Count Asterisks

# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

# Return the number of '*' in s, excluding the '*' between each pair of '|'.

# Note that each '|' will belong to exactly one pair.

def countAsterisks(s):
    count = 0
    lcount = 0
    for i in range(len(s)):
        if s[i] == '*' and lcount == 0:
            count += 1
        elif s[i] == '|' and lcount == 0:
            lcount += 1
        elif s[i] == '|' and lcount != 0:
            lcount = 0
    return count

# 1021. Remove Outermost Parentheses

# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

def removeOuterParentheses(s):
    out = ''
    count = 0
    for char in s:
        if char == '(':
            count += 1
            if count != 1:
                out += '('
        elif char == ')':
            count -= 1
            if count != 0:
                out += ')'
    return out
