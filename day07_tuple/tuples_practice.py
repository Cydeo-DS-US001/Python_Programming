
group1 = ('Aaron', 'Breanna', 'James')
group2 = ('Asel', 'Yulia', 'Shay', 'Ahmet')
group3 = ('Conor', 'John', 'Daniel', 'Muhtar', 'Max')

groups = ( group1, group2, group3)

print(groups)

print('----------------------------------------------------------')

for each_group in groups:  # to access each tuples in the nested tuple groups
    for each_student in each_group: # to access each string in each tuple
        print(each_student)

print('----------------------------------------------------------')

students = group1 + group2 + group3

print(students)

print('----------------------------------------------------------')

fruits = ('Orange', 'Cherry', 'Lemon', 'Apple', 'Strawberry')

result = fruits * 3

print(result)

print('----------------------------------------------------------')

numbers = (100, 200, 300, 400)
# numbers[0] = 1000
print(numbers)



