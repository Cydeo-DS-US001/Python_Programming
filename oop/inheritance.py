class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f'{self.name} is eating')

    def drink(self):
        print(f'{self.name} is drinking water')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def __str__(self):
        return f'name: {self.name}, age: {self.age}, gender: {self.gender}'


class Employee(Person):

    def __init__(self, name, age, gender, job_title, salary, company, is_full_time):
        super().__init__(name, age, gender)
        self.job_title = job_title
        self.salary = salary
        self.company = company
        self.is_full_time = is_full_time

    def work(self):
        print(f'{self.job_title} {self.name} is working')

    def __str__(self):
        return f'{type(self).__name__}[{super().__str__()}, job_title: {self.job_title}, salary: {self.salary}, full time: {self.is_full_time}]'


class Teacher(Employee):
    def work(self):
        print(f'Teacher {self.name} is teaching in the class')


class Driver(Employee):
    def work(self):
        print(f'Driver {self.name} is driving on the road')


class Developer(Employee):
    def work(self):
        print(f'Developer {self.name} is coding')




"""

teacher = Teacher('James', 35, 'Male', 'High School Teacher', 80_000, 'Houston High School', True)
teacher.work()
teacher.eat()
teacher.drink()
teacher.sleep()

print(teacher)

developer = Developer('Bella', 29, 'Female', 'Python Developer', 100_000, 'Apple Inc', False)
print(developer)



"""

"""
Employee:
    Attributes: job_title, salary, company, is_full_time
    methods:  work()

Teacher:
    Attributes: 
    methods:

Driver:
    Attributes:
    methods:

Developer:
    Attributes:
    methods: 
    
...

"""
