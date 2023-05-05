class Dog:

    def __init__(self, name, breed, gender, size, age, color):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.size = size
        self.age = age
        self.color = color

    def eat(self):
        print(f'{self.name} is eating')

    def drink(self):
        print(f'{self.name} is drinking')

    def __str__(self):
        return f'Dog name: {self.name}, gender: {self.gender}'


dog1 = Dog("Lessy", "Corgi", "Female", "Small", 1, "Gold and White")
dog2 = Dog("Max", "Husky", "Male", "Large", 3, "White")

dog1.eat()
dog2.drink()

print(dog1)
print(dog2)
