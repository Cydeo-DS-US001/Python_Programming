import json


cars = {
    "cars": [
        {"make": "BMW", "model": 'X5'},
        {"make": "Audi", "model": 'Q6'},
        {"make": "Tesla", "model": 'Model-Y'},
        {"make": "Lexus", "model": 'RX450'}
    ]
}

json_file = open('/Users/cydeo/PycharmProjects/Python_Programming/day12_file_handling/json/cars.json', 'w')

json_obj = json.dumps(cars, indent=4)

json_file.write(json_obj)


print('------------------------------------------------------------------')

json_file = open('/Users/cydeo/PycharmProjects/Python_Programming/day12_file_handling/json/cars.json', 'r')

cars = json.load(json_file)

print(cars)

print(cars['cars'])

print('------------------------------------------------------------------')

for p in cars['cars']:
    print(p)
