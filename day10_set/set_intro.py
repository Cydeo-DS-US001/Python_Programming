
numbers = {10, 10, 20, 20, 30, 30, 40, 40}

print(numbers)

numbers.add(50)

print(numbers)

numbers.add(10)

print(numbers)

print( len(numbers))

numbers.add('Python')

numbers.add(True)

print(numbers)

# print(numbers[1])

print('-------------------------------------------------')

for x in numbers:
    print(x)

print('-------------------------------------------------')

nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]

even_nums = list( {x for x in nums if x % 2 == 0} )

odd_nums = list( {x for x in nums if x % 2 != 0} )


print(even_nums)

print(odd_nums)

print(even_nums[0])
print(odd_nums[0])

print('-------------------------------------------------')
