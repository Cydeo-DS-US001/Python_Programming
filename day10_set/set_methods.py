# add(): adds the specified element into the Set
subjects = set()

print(subjects)

subjects.add('Python')
subjects.add('Apple')
subjects.add('Java')

print(subjects)


# clear(): removes all the elements from the Set

print( len(subjects))

subjects.clear()

print( len(subjects))
print(subjects)

print('-----------------------------------------')

# pop(): removes the first element from the set
numbers = {10, 20, 30, 40, 50, 60}

print(numbers)

numbers.pop()

print(numbers)

numbers.pop()

print(numbers)

print('-----------------------------------------')
# copy(): returns a new Set by copying all the elements of the Set
"""
numbers1 = {1, 2, 3, 4, 5, 6}
numbers2 = numbers1

numbers1.add(100)

print(numbers1)
print(numbers2)
"""
numbers1 = {1, 2, 3, 4, 5, 6}
numbers2 = numbers1.copy()

numbers1.add(100)

print(numbers1)
print(numbers2)

print('-----------------------------------------')

# remove(): removes the specified element from the Set
words = {'Python', 'Java', 'Cydeo', 'Wooden Spoon'}

print(words)

words.remove('Java')

print(words)

print('-----------------------------------------')

# difference(): compares two sets and returns a new set which contains the items that only exist in first set
s1 = {'Java', 'Python', 'C#'}
s2 = {'Ruby', 'Java', 'C++', 'Swift'}

s3 = s1.difference(s2)  # returns the elements that are only unique to s1 compare to s2

print(s3)

print('-----------------------------------------')

# intersection(): compares two sets and returns a new set which contains the common elements of two sets
set1 = {'Java', 'Python', 'C#', 'Cydeo'}
set2 = {'C++', 'Ruby', 'Swift', 'Java', 'Python'}

set3 = set1.intersection(set2)

print(set3)

print('-----------------------------------------')

# different_update(): removes the elements of the first Set that exist in the second Set
a1 = {'Book', 'Pen', 'Apple', 'Cherry', 'Coffee'}
a2 = {'Book', 'Apple', 'Banana', 'Grape', 'TV'}

a1.difference_update(a2)  # updates the set a1 by removing the elements that are included in set a2

print(a1)

print('-----------------------------------------')

# intersection_update(): removes the uncommon elements of first & second sets
b1 = {'Cydeo', 'Python', 'Java', 'C#', 'Wooden Spoon', 'Ruby', 'Swift'}
b2 = {'Wooden Spoon', 'Python', 'Cydeo'}

b1.intersection_update(b2)

print(b1)

print('-----------------------------------------')

# symmetric_difference(): Compares two sets and returns a new set which contains all elements except the common once
e1 = {'Apple', 'Banana', 'Cherry'}
e2 = {'Grape', 'Strawberry', 'Banana', 'Mango', 'Lemon', 'Apple'}

e3 = e1.symmetric_difference(e2)

print(e3)