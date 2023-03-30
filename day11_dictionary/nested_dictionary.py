tuple1 = (1, 2.5, 'Python', True, (10, 20, 30), [25, 30, 40], {1, 1, 1, 1, 2, 2})

print(len(tuple1))
print(tuple1)

list1 = [1, 2.5, 'Python', True, (10, 20, 30), [25, 30, 40], {1, 1, 1, 1, 2, 2}]

print(len(list1))
print(list1)

print('-----------------------------------------------------------------------')

employees = {
    'B1': {
        'name': 'James',
        'job_title': 'Data Analyst',
        'salary': 100000
    },

    'B2': {
        'name': 'Yulia',
        'job_title': 'Python Developer',
        'salary': 110000
    },

    'B3': {
        'name': 'Bella',
        'job_title': 'Scrum Master',
        'salary': 900000
    }
}

print(employees)
print(employees['B1']['name'])

print('-----------------------------------------------------------------------')

for v in list(employees.values()): # gets each inner dictionary
    for k in list(v.keys()): # get each keys from each inner dictionary
        if str(k) == 'name':  # if the key is equal to name
            print(v[k])  # getting the value of the key 'name'


print('-----------------------------------------------------------------------')

for p in list(employees.items()):
    print(p[1]['name'])


















