
str = "aaabbcccc"

result = ""  #'ab'

"""
for x in str:  # x : each character of str
    if x in result:  # if the character is already included in the string result
        continue  # skip
    result += x
"""

for x in str:  # x : each character of str
    if x not in result:  # if the character is not included in the string result yet
        result += x

print(result)

"""
Write a program that can remove all the duplicated characters from a string
    Ex:
        str = "aaabbcccc"

        Output:
            abc
"""
