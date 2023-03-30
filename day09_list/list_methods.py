# append(): adds the specified element to the List
names = ['Ahmed', 'Muhtar', "Lucy", 'Bella', "James", "Josh"]

print(names)

names.append('Aaron')

print(names)

#  clear(): removes all the elements of the List

names.clear()

print(names)
print( len(names))

print('-------------------------------------------------------------')

# extend(): adds the specified collection of elements to the List
students = ['Yulia', 'Muhtar', 'Aaron', 'Danilo', 'Bella']

print(students)
group1 = ['Shay', 'Emma']
group2 = ('Conor', 'Nick', "Jon")

students.extend(group1)

print(students)

students.extend(group2)

print(students)

print('-------------------------------------------------------------')
# sort() sorts the list in ascending order
numbers = [65, 34, 45, 100, 95, 85, 20, 10, -5, -2]

print(numbers)

numbers.sort()

print(numbers)

n = [40, 50, 10, 15, 5, 4, 3, 100]
n.sort(reverse=True)
print(n)

print('-------------------------------------------------------------')

# reverse(): reverses the elements of the list
words = ['Java', 'SQL', 'Cydeo', 'Wooden Spoon', 'Python']
print(words)

words.reverse()

print(words)

print('-------------------------------------------------------------')

# copy(): returns a new list by copying all the elements of the list
list1 = ['A', 'B', 'C', 'D', 'E']
list2 = list1.copy() # new list object

print(list2)

print('-------------------------------------------------------------')

# remove(): removes the specified element from the List
employees = ['James', 'Ahmed', 'Breanna', 'Yulia', 'Josh', 'Jerry', 'Ahmed']
employees.remove('Ahmed')

print(employees)

print('-------------------------------------------------------------')

# pop(): by default removes the last inserted element. if index is specified, removes the element at that index
scores = [15, 25, 35, 45, 55, 65, 75, 85]
print(scores)

scores.pop() # removes the last element

print(scores)

scores.pop(1)

print(scores)

scores.pop(-2)

print(scores)

print('-------------------------------------------------------------')

# insert(): inserts the specified element at the specified index
elements = ['Python', 'Java', 'Wooden Spoon', 'SQL']

elements.insert(2, 'Cydeo')

print(elements)

print('-------------------------------------------------------------')

# index(): returns the index number of the specified element
subjects = ['Mathematics', 'Physics', 'Biology', 'Chemistry', 'Programming']

has_Cydeo = 'Cydeo' in subjects

print(has_Cydeo)

a = subjects.index('Programming')

print(a)

print('-------------------------------------------------------------')

# count(): returns the frequency of the specified element

numbers = [10, 20, 30, 10, 10, 10, 50, 60, 70]

count10 = numbers.count(10)

print(count10)


