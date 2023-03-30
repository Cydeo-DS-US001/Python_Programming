# step 2: import json module
import json

# step 1: open the json file
json_file = open('/Users/cydeo/PycharmProjects/Python_Programming/day12_file_handling/json/students.json', 'w')

students_info = {
    "s1": {"name": "James", 'age': 19, "gpa": 3.5},
    "s2": {"name": "Isabella", 'age': 23, "gpa": 3.8}
}

# json_file.write(students_info)

# step 3: dictionary to json
json_object = json.dumps(students_info, indent=4)

# step 4: write it to the json file
json_file.write(json_object)
