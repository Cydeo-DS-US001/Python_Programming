age = int( input('Enter your age:\n') )

while age < 0 or age > 150:  # while the age is invalid
    age = int( input('Invalid entry! Please re-enter your age:\n') )

print(f'You are {age} years old')


"""
Ask user to enter your age and display the age of the user
    If user enters invalid number for the age (less than zero or greater than 150),
    then ask the user to re-enter his/her age until user enters a valid age

    Ex:
        Input:
            Enter your age:
            -5
            Invalid entry, please re-enter your age:
            25

        Output:
            You are 25 years old

"""