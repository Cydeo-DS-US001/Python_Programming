def is_palindrome(string):
    if type(string) is not str: # if the given argument is NOT a string
        return False # exits the function and return false

    reversed_string = string[::-1]  # reversing the given argument
    # reversed_string = reversed( str(string) )

    return str(reversed_string).lower() == str(string).lower()


def sum_of_digits(string):
    sum = 0
    for x in string:  # to access each value of string
        if str(x).isdigit():  # if the character is digit
            sum += int(str(x))  # construct an integer from that digit character
    return sum


def print_each(sequence):
    for x in sequence:
        print(x)