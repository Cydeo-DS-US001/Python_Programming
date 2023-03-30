
number = 0 # to store the user entered numbers when the loop starts
sum_of_positive_nums = 0 # to stopre the sum of positive numbers that user entered

while number >= 0: # while the number is not negative
    number = int(input('Enter a number:\n'))
    if number > 0: # if user enters a positive
        sum_of_positive_nums += number

print(f'Sum of positive numbers: {sum_of_positive_nums}')


"""
Write a program that asks user to enter a number until user enters a negative number.
returns the sum all the positive numbers uer entered

        Ex:
            Input:
                Enter a number:
                10
                Enter a number:
                20
                Enter a number:
                -10

            Output:
                30
"""