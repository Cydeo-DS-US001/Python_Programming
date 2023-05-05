class Person:

    def __init__(self):
        self.__name = None
        self.__age = None

    def get_name(self):
        if self.__name is None:
            raise RuntimeError('Name has not been set')
        return self.__name

    def set_name(self, name):
        if len(name) == 0:
            raise RuntimeError('Name can not be empty')
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise RuntimeError('Age can not be negative')
        self.__age = age



person1 = Person()

person1.set_name('James')
person1.set_age(-100)

print(person1.get_name())
print(person1.get_age())
