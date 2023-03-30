student1 = {
    'name': 'Isabella',
    'age': 29,
    'from': 'USA',
    'full_time': True,
    'gpa': 3.5
}

# get(): returns the value of specified key
age = student1.get('age')
print(age)

age = student1['age']
print(age)

# update(): updates the specified pair (key&value). If the pair does not exist then adds it to dictionary
student1.update( {'gpa': 2.5, 'school': 'MIT'} )
print(student1)

student1['gpa'] = 3.5
print(student1)

student1['gender'] = 'Female'
print(student1)

# pop(): removes the pair with the specified key

student1.pop('school')
print(student1)

# popitem(): removes the last inserted pair

student1.popitem()
print(student1)


# clear(): removes all the pairs from the dictionary

print(len(student1))

student1.clear()

print(len(student1))

print(student1)

print('-----------------------------------------------')

# copy(): returns a new dictionary by copying all the pairs of the dictionary

student2 = {
    'name': 'Aaron',
    'age': 28,
    'from': 'Canada',
    'full_time': True,
    'gpa': 3
}

# student3 = student2
student3 = student2.copy()  # new dictionary object is created

student2.update( {'age': 35} )

print(student2)
print(student3)


# keys(): returns all the keys of dictionary as a list

keys_list = list(student3.keys())

print(keys_list)
print(keys_list[2])


# values(): returns all the values of dictionary as a list

values_list = list( student3.values() )

print(values_list)

print(values_list[2])


# items(): returns all the pairs (each pair as a tuple) as a list

paris_list = list( student3.items())

print(paris_list)

print(paris_list[-1])

print(paris_list[-1][0])


