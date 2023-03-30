def greetings():
    print('Hello Everyone!')
    print('How are you today?')
    print('Wish you have a wonderful day!')


greetings()
# greetings()
# greetings()

print('Task Completed')

print('-----------------------------------------------------')


# create a function that prints all the odd numbers between 1 ~ 100
def print_odd_1to100():
    result = ''

    for x in range(1, 101):
        if x % 2 != 0:  # if the number can not be evenly divisible by 2, then it's odd number
            result += str(x) + ' '

    print(result)


print_odd_1to100()


# create a function that can print all the even numbers between 1 ~ 100
def print_even_1to100():
    result = ''

    for x in range(1, 101):
        if x % 2 == 0:  # if the number can be evenly divisible by 2, then it's even number
            result += str(x) + ' '

    print(result)


print_even_1to100()

print('-----------------------------------------------------')

greetings()

print('-----------------------------------------------------')

print_odd_1to100()

print('-----------------------------------------------------')
print_even_1to100()
