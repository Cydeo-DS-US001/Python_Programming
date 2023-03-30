
students = {
    's1': {
            'name': 'Josh',
            'gpa': 2.5,
            'subjects': ['Math', 'Physics']
    },

    's2': {
        'name': 'Breanna',
        'gpa': 3.5,
        'subjects': ['Biology', 'Chemistry']
    }

}

for p in list(students.items()):
    p[1]['subjects'] = p[1]['subjects'] + ['Programming']

print(students)

print('------------------------------------------------------------------')
for p in list(students.items()):
    print( f'{p[1]["name"]}  -  {p[1]["gpa"]}' )
