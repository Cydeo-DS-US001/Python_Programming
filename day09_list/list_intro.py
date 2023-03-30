
groceries_list = ['Eggs', 'Apples', 'Rice', 'Milk']

print( len(groceries_list))

print(groceries_list)

groceries_list.append('Beef')

print( len(groceries_list))

print(groceries_list)

groceries_list[0] = "Cherry"

print(groceries_list)

groceries_list[-1] = "Chicken"

print(groceries_list)

print( groceries_list[-2])
print( groceries_list[1])

print('-----------------------------------------------------')

numbers = [75, 85, 95, 100, 105, 110]

list1 = numbers[1:4]

print(list1)

list2 = numbers[:4]

print(list2)

list3 = numbers[2:]

print(list3)

reversed_numbers = numbers[::-1]

print(reversed_numbers)

reversed_numbers = list(reversed(numbers))

print(reversed_numbers)

print('-----------------------------------------------------')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters[1:4] = ['B', 'C', 'D']

print(letters)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

numbers[:5] = [100, 200, 300, 400, 500]

print(numbers)

numbers[5:] = [600, 700, 800, 900, 1000, 2000, 3000, 4000]

print(numbers)

print('-----------------------------------------------------')

names = ['Java', 'Python', 'Cydeo', 'Wooden Spoon']

for x in names: # x: each element of the names list
    print(x)

print('-----------------------------------------------------')

for i in range(0, len(names)): # i: forward index numbers of the names list
    if type(names[i]) == str: # if the element at index i is a string
        names[i] = names[i].upper() # create the uppercase version of the string at index i, and update the index i

print(names)

print('-----------------------------------------------------')

numbers = [10, 20, 30, 40, 50, 60, 70]

for i in range(0, len(numbers)): # i: forward index numbers of the numbers list
    if type(numbers[i]) == int: # if the element at index i is an integer
        numbers[i] = numbers[i] * 10 # multiply the element at index i by 10 and update the index i

print(numbers)


