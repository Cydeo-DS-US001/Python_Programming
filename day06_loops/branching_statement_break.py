for i in range(1, 11):
    print(i)
    if i == 5:
        break  # exits the loop

print('----------------------------------------------------------')

str = 'ABCDEFJHI'

for each_char in str:
    print(each_char)
    if each_char == 'E':
        break

print(' -------------------------------------------------------- ')

sum_of_positive_nums = 0

while True:
    number = int(input('Enter a number:\n'))
    if number >= 0:
        sum_of_positive_nums += number
    else:  # if user enters negative number
        break  # exits the loop

print('Task Completed')
