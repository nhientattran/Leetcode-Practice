# Given a number N, for each integer i in the range from 1 to N inclusive, print one value per line as follows:
# • If i is a multiple of both 3 and 5, print FizzBuzz.
# • If i is a multiple of 3 but not 5, print Fizz.
# • If i is a multiple of 5 but not 3, print Buzz.
# • If i is not a multiple of 3 or 5, print the value of i.
# Write an algorithm which follows the given instructions and prints the required output.

def fizz_buzz(n):
    out = ''
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            out += 'FizzBuzz\n'
        elif num % 3 == 0:
            out += 'Fizz\n'
        elif num % 5 == 0:
            out += 'Buzz\n'
        else:
            out += str(num) + '\n'
    return out

# Write an algorithm to find the sub-string from the given string that is the same when read forwards and backwards.
# Input
# The input consists of a string, representing the given string for the puzzle.
# Output
# From the given string, print a sub-string which is the same when read forwards and backwards.
# Note
# If there are multiple sub-strings of equal length, choose the lexicographically smallest one.
# If there are multiple sub-strings of different length, choose the one with maximum length.
# If there is no sub-string that is the same when read forwards and backwards print "None".
# Sub-string is only valid if its length is more than 1.
# Strings only contain uppercase characters (A-2).

def sub_string_finder(strs):
    n = len(strs)
    max_length = 0
    out = ''
    for i in range(n):
        for j in range(i + 2, n):
            sub_string = strs[i:j]
            if sub_string == sub_string[::-1] and len(sub_string) > max_length:
                max_length = len(sub_string)
                out = sub_string
    if out:
        return out
    else:
        return None

# Write an algorithm which finds out the elements which are largest in a row and smallest in a column in a matrix.
# Input
# The first line of input consists of two space-separated integers-
# matrix_row and matrix_col, representing the number of rows in the matrix 👎 and the number of columns in the matrix (M), respectively.
# The next M lines consist of N space-separated integers representing the elements of the matrix.
# Output
# Print a number which is largest in a row and smallest in a column in the given matrix. If no element is found print '-1'

def martrix_element(martrix):
    rows = len(martrix)
    columns = len(martrix[1]) 
    largest_in_row = [max(row) for row in martrix]
    smallest_in_col = [min(martrix[i][j] for i in range(rows)) for j in range(columns)]
    for i in range(rows):
        if largest_in_row[i] in smallest_in_col:
            return largest_in_row[i]
    return -1