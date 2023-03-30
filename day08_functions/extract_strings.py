
elements = (10, 2.5, 300, 'Python', 'Java', True, False, 300, 'Cydeo', 'WoodenSpoon', 100)

# print( type(elements[3]) == str)

for x in elements: # x: each element of the tuple elements
    if type(x) == str: # if the element's type is string
        print(x)

"""
Write a program that can extract the strings from a tuple
    Ex:
        elements = (10, 2.5, 300, 'Python', 'Java', True, False, 300)

        Output:
             Python
             Java
"""

