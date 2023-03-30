
names = ('Ahmet', 'James', 'Ahmet', 'Daniel', 'Josh', 'Breanna', 'Bella', 'Shay', 'Yulia', 'Ahmet')

index1 = names.index('Daniel')
index2 = names.index('Shay')
print(index1)
print(index2)

special_students = names[names.index('Daniel') : names.index('Shay')+1]

print(special_students)

count_ahmet = names.count('Ahmet')

print(count_ahmet)

print('---------------------------------------------------------------')

words = ('Python', 'Java', 'Java', 'Python', 'C#', 'C++', 'SQL', 'JavaScript', 'Swift', 'Python', 'Python')

count_python = words.count('Python')
count_java = words.count('Java')

print(f'Total number of Java: {count_java}')
print(f'Total number of Python: {count_python}')

is_even = count_java == count_python

print(is_even)


