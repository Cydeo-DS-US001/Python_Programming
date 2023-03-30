cars = [
    {'make': 'Mercedes', 'model': 'C-Class', 'year': 2022, 'price': 55000, 'ev': False, 'color': 'Blue'},
    {'make': 'BMW', 'model': 'X6', 'year': 2021, 'price': 65000, 'ev': False, 'color': 'Red'},
    {'make': 'Tesla', 'model': 'Model Y', 'year': 2020, 'price': 95000, 'ev': True, 'color': 'White'},
    {'make': 'Nio', 'model': 'ES7', 'year': 2022, 'price': 85000, 'ev': True, 'color': 'Gray'},
    {'make': 'Lucid', 'model': 'Air', 'year': 2022, 'price': 105000, 'ev': True, 'color': 'Black'},
    {'make': 'Polestar', 'model': '2', 'year': 2021, 'price': 85000, 'ev': True, 'color': 'Yellow'},
    {'make': 'Honda', 'model': 'Accord', 'year': 2019, 'price': 35000, 'ev': False, 'color': 'Gold'},
    {'make': 'Toyota', 'model': 'Camry', 'year': 2018, 'price': 28000, 'ev': False, 'color': 'Gold'},
    {'make': 'Nissan', 'model': 'Ultimate', 'year': 2017, 'price': 25000, 'ev': False, 'color': 'Gold'},
]

for d in cars:
    print(f'{d["year"]} {d["make"]} {d["model"]} ${d["price"]}')

print('-----------------------------------------------------------------------')

for d in cars:
    if d['ev']:
        print(f'{d["make"]} {d["model"]}')

print('-----------------------------------------------------------------------')

for d in cars:
    if d['price'] < 60000:
        print(f'{d["make"]} - {d["model"]} - ${d["price"]}')

"""
A list of dictionary that contains the car information is given
    1.Display the make, model, year and price  of each car in separate lines in the following format:
                        year make model $price
                        
    2. Display the make and model of all the electric cars
   
    3. Display the make, model and price of the cars that are under $60k
"""
