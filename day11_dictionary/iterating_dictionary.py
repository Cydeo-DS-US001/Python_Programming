car1 = {
    'make': 'Toyota',
    'model': 'Camry',
    'year': 2020,
    'color': 'White',
    'price': 30000
}

# iterating dictionary by keys
for k in list(car1.keys()):
    print(f'{k} -  {car1[k]}')

print("-----------------------------------------")

# iterating dictionary by values
for v in list(car1.values()):
    print(v)

print("-----------------------------------------")
# iterating dictionary by pairs
for p in list(car1.items()):
    print(f'{p[0]} - {p[1]}')