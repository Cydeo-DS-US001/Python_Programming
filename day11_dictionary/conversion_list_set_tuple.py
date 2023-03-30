# converting tuple to list & set
nums = (10, 20, 30, 40, 50, 10, 20, 10, 20)

list1 = list(nums)  # constructs a list from the tuple nums
set1 = set(nums)  # constructs a set from the tuple nums

print(list1)
print(type(list1))

print(set1)
print(type(set1))

print('-----------------------------------------------------------------')

# converting list to tuple & set

nums = [10, 20, 30, 40, 50, 10, 20, 10, 20]

tuple2 = tuple(nums)  # constructs a tuple from the list nums
set2 = set(nums)  # constructs a set from the list nums

print(tuple2)
print(set2)

print('-----------------------------------------------------------------')

# converting set to tuple & list

nums = {10, 20, 30, 40, 50, 10, 20, 10, 20}

tuple3 = tuple(nums)  # constructs a tuple from the set nums
list3 = list(nums)  # constructs a list from the set nums

print(tuple3)
print(list3)

print('-----------------------------------------------------------------')

numbers = (1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 8, 9, 10)

result = tuple({x for x in numbers if x < 5})
# a tuple will be constructed from the set that was generated using the comprehensions

print(result)
