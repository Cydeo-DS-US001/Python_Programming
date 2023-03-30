#          0          1           2            3          4         5           6
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
#         -7          -6          -5          -4         -3         -2        -1
print(len(days))
print(days)

print(days[1])  # returns the second element from the tuple days
print(days[-2])  # returns the second last element from the tuple

print('----------------------------------------------')

for x in days:  # accesses each element of the tuple
    print(x)  # prints each element of tuple

print('----------------------------------------------')

working_days = days[1:5]  # Slices the tuple days starting from index 1 to index 5 (excluded) and returns new tuple
print(working_days)

tuple1 = days[2: 5 + 1]  # Slices the tuple days starting from index 2 to index 6 (excluded) and returns new tuple
print(tuple1)

print('----------------------------------------------')

# business_days = days[:5]
business_days = days[:-2]  # Slices the tuple days starting from first element to the element at index -2 (excluded)
print(business_days)

print('----------------------------------------------')

# weekend_days = days[5:]
weekend_days = days[-2:]  # Slices the tuple days starting from index -2 to the end of the tuple
print(weekend_days)

tuple2 = days[3:]  # Slices the tuple days starting from index 3 to the end of the tuple
print(tuple2)

print('----------------------------------------------')

reversed_tuple = days[::-1]
# Slices the tuple starting from last element and stores the elements in sliced order to the new tuple

print(reversed_tuple)

print('----------------------------------------------')

print(tuple(range(1, 10)))  # constructs a tuple from the range of values 1 ~10

print(tuple(reversed(days)))  # constructors a tuple which has the reversed object of the tuple days

print('----------------------------------------------')

for y in tuple(reversed(days)): # accesses each element of the tuple which is the reversed version of the tuple days
    print(y)
