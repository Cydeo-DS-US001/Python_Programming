def sum_of_digits(string):
    sum = 0
    for x in string:  # to access each value of string
        if str(x).isdigit():  # if the character is digit
            sum += int(str(x))  # construct an integer from that digit character
    return sum


a = sum_of_digits("a1b2c3d4t1")

print(a)

"""
Create a function named sum_of_digits that takes an argument of string
    The function returns the sum of all digit characters from the string

    Ex:
        sum_of_digits("a1b2c3") ===> 6

        sum_of_digits("abcdefg) ===> 0
"""
