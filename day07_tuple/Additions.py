
while True:
    first_number = float(input('Enter your first number:\n'))
    second_number = float(input('Enter your second number:\n'))

    print(f'The addition of {first_number} and {second_number} is equal to {first_number+second_number}')

    answer = input('Would you like to continue? (Yes/No)\n').lower()

    while not (answer == 'yes' or answer == 'no'): # while the answer is not valid
        answer = input('Invalid entry, Please re-enter! Would you like to continue? (Yes/No)\n').lower()

    if answer == 'no':  # if the user does not want to continue
        print('Thanks for using Cydeo Calculator')
        break # exits the loop


"""
Write a program that can calculate the addition of any user entered two numbers.
    1 ask the user to enter the first number (float)
    2 ask the to enter the second number (float)
    3 display the addition of those two numbers
    4 Ask the user: "Would you like to continue? (Yes/No)"
        If user enters yes, repeat the whole steps again
        If user enters no then display "Thanks for using Cydeo Calculator"

        If the user enters an invalid entry (other than yes or no) then ask the user to re-enter until user enters the valid input
"""
