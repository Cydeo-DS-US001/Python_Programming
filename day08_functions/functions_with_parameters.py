def display_value(value):
    print(f'The value is {value}')


display_value('Python')

name = 'Java'

display_value(name)

display_value(100)

display_value(True)

display_value(20.5)

display_value((1, 2, 3))

print('-------------------------------------------------------------------')


def eligible_to_buy_alcohol(age):
    if type(age) == int:  # if the argument that's given to age is an integer
        if age >= 21:
            print('You are eligible to buy alcohol')
        else:
            print('You are not eligible to buy alcohol')
    else:  # if the argument that's given to the age is not an integer
        print('Invalid data for the age!')


eligible_to_buy_alcohol('Python')
eligible_to_buy_alcohol(19)
eligible_to_buy_alcohol(42)

print('-------------------------------------------------------------------')


def find_max_num(n1, n2):
    if n1 > n2:
        print(f'{n1} is greater')
    elif n2 > n1:
        print(f'{n2} is greater')
    else:
        print('Both are equal')


find_max_num(10, 20)

find_max_num(100, 100)

find_max_num(1000, 500)

print('-------------------------------------------------------------------')


def print_each(sequence):
    for x in sequence:
        print(x)


word = 'Wooden Spoon'

names = ('James', 'Bella', 'Yulia', 'Aaron')

print_each(names)

print('-------------------------------------------------------------------')


# create a function that can calculate the grade of the student based on the score

def grade(score):
    result = None
    if 0 <= score <= 100:  # score is valid

        if score >= 90:
            result = 'A'
        elif score >= 80:
            result = 'B'
        elif score >= 70:
            result = 'C'
        elif score >= 60:
            result = 'D'
        else:
            result = 'F'

    else:  # score is invalid
        result = 'Invalid score'

    print(result)


grade(150)





