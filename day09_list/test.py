import string_utility as su
import math_utility as mu

s = 'racecar'

r = su.is_palindrome(s)

print(r)

print('---------------------------------------')

n = 'C2y4d6e8o'

sum = su.sum_of_digits(n)

print(sum)

print('---------------------------------------')

word = 'Python'

su.print_each(word)

print('---------------------------------------')

n = 20

result = mu.square(n)

print(result)


m = 5

result = mu.cube(m)

print(result)

