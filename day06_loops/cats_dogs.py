sentence = 'CAT cat cAT DOG dog dOG Dog cAT cat cat CAT'

cats = sentence.lower().count('cat')
dogs = sentence.lower().count('dog')

print(f'Total number of cats: {cats}')
print(f'Total number of dogs: {dogs}')

even = cats == dogs

print(even)

"""
2. Create a python file named cats_dogs.py
    2.2 a string variable named sentence is already declared and given
    2.3 Write a program that can check if the total number of 'cat' and 'dog' are even in the given string, print True if they are even, otherwise print false

        Ex:
            sentence = 'CAT cat cAT DOG dog dOG Dog cAT'

            output:
                True
"""
