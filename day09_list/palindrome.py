
def is_palindrome(string):
    if type(string) is not str: # if the given argument is NOT a string
        return False # exits the function and return false

    reversed_string = string[::-1]  # reversing the given argument
    # reversed_string = reversed( str(string) )

    return str(reversed_string).lower() == str(string).lower()


print( is_palindrome('Level') )
print( is_palindrome('Python'))
print( is_palindrome(123))



"""
Create a function named is_palindrome that takes one string argument
    The function checks if the given string argument is palindrome, returns true if it is
    otherwise returns false

    if the given argument is not a string, the function returns false by default

        Ex:
            is_palindrome("Level") ====> True

            is_Palindrome("python") ====> False

    Hint: palindrome string is the string that reads the same backward as forward
    
    Level ===> leveL
    Anna  ===> annA

"""