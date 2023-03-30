
first_name = input('Enter your first name:\n')
last_name = input('Enter your last name:\n')

"""
first_name = first_name.capitalize()
last_name = last_name.capitalize()
print(f'Your full name is {first_name} {last_name}')
"""

full_name = first_name + ' ' + last_name
full_name = full_name.title()

print(f'Your full name is {full_name}')



"""
1. Create a python file named full_name.py
    1.1 Write a program that asks user to enter his/her first and last names
    1.2 print the full name of the person in regular format

        Ex:
            Enter your first name:
            cYdEo
            Enter your last name:
            SCHOOL

            output:
                Your full name is Cydeo School
"""
