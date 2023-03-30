word = input('Enter a word:\n')

first_character = word[:1]

if first_character.isdigit():  # if the first character is a digit
    print('first character is digit')
elif first_character.isupper():  # if the first character is uppercase letter
    print('first character is uppercase letter')
elif first_character.islower():  # if the first character is lowercase letter
    print('first character is lowercase letter')
else:  # if the character is special character
    print('first character is special character')

"""
3. Create a python file named first_character.py
    3.1 Ask the user to enter a word
        if the word starts with digits, print "first character is digit"
        if the word starts with uppercase letters, print "first character is uppercase letter"
        if the word starts with lowercase letters, print "first character is lowercase letter"
        if the word starts with special characters, print "first character is special character"
"""
