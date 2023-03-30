# step 2: import the json module (module that's designed for handling json objects
import json

# step 1: Open the json file
json_file = open('/Users/cydeo/PycharmProjects/Python_Programming/day12_file_handling/json/employees.json', 'r')
# print(json_file.read())

# step 3: load the json file (convert the json object to dictionary object)
employees_info = json.load(json_file)

print( type(employees_info) )
print(employees_info)

print("-----------------------------------")

print(employees_info['A01']['name'])
