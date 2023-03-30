nums = []

for x in range(1, 51):
    nums.append(x)

print(nums)

print('---------------------------------------------------------------------------------')

"""
odd_nums = list()

for x in nums:
    if x % 2 != 0:
        odd_nums.append(x)
"""

odd_nums = [x for x in nums if x % 2 != 0]  # x:  each element of nums list that are Odd

print(odd_nums)

print('---------------------------------------------------------------------------------')

even_nums = [e for e in nums if e % 2 == 0]  # e: each element of nums list that are even

print(even_nums)

print('---------------------------------------------------------------------------------')

words = ('Java', 'Python', 'Python', 'JavaScript', 'Ruby')

new_tuple = tuple([x for x in words if x.startswith('J')])  # x: Elements of the list words that starts with J
# list is converted to tuple. we need to get the list first because comprehension is not supported with tuple


print(new_tuple)

new_list = [x for x in words if x.startswith('J')]  # x: Elements of the list words that starts with J

print(new_list)

print('------------------------------------------------------------------------------')

numbers = [10, 20, 10, 30, 30, 40, 40, 40, 40, 500, 50, 50, 600, 700]

unique_elements = [x for x in numbers if numbers.count(x) == 1]  # x: unique elements of the list numbers

print(unique_elements)

print('---------------------------------------------------------------------------------')

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tuple1 = tuple( [x for x in nums if x > 5] )

print(tuple1)
