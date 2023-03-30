
employee1 = {
    "name": 'James',
    'age': 35,
    'job_title': 'Developer'
}

print(employee1)
print(employee1['name'])  # prints the value of the key 'name' of the dictionary employee1

print(len(employee1))  # displays the number of pairs of the dictionary employee1

employee1['company'] = 'Apple Inc'  # adds the pair 'company: Apple Inc' to the dictionary employee1

print(employee1)

employee1['job_title'] = 'Data Analyst'  # adds the pair 'job_title: Data Analyst' to the dictionary employee1
employee1['company'] = 'Google Inc'  # updates the value of the pair with key of 'company' to 'Google Inc'

employee1['salary'] = 100_000  # adds the pair 'salary: 10000' to the dictionary employee1

print(employee1)
