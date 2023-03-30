employees = [
    {'name': 'James', 'age': 29, 'job_title': 'Data Analyst', "salary": 95000},
    {'name': 'Isabella', 'age': 28, 'job_title': 'Software Developer', "salary": 130000},
    {'name': 'Daniel', 'age': 35, 'job_title': 'Software Engineer', "salary": 100000},
    {'name': 'Yulia', 'age': 32, 'job_title': 'Business Analyst', "salary": 110000},
    {'name': 'Aaron', 'age': 45, 'job_title': 'Cybersecurity Specialist', "salary": 125000},
    {'name': 'Shay', 'age': 36, 'job_title': 'Scrum Master', "salary": 90000},
]

for d in employees:
    print(f"{d['name']} - {d['job_title']}")

print('--------------------------------------------------------------------')

for d in employees:
    if d['salary'] >= 120_000:
        print(d['name'])

print('--------------------------------------------------------------------')

for d in employees:
    if d['job_title'] == 'Software Developer':
        print(d['name'])


"""
A list of dictionary that contains all the employee info is given
    1.Display the name and job title of each employee in separate lines in the following format:
                        name - job title
                        
    2. Display the names of the employees who has salary of 120k or more
   
    3. Display the names of all the software developers           
"""
