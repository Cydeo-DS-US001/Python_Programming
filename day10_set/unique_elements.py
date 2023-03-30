numbers = [10, 20, 10, 30, 30, 40, 40, 40, 40, 500, 50, 50, 600, 700]

unique_elements = list()

for x in numbers:
    if numbers.count(x) == 1:  # if the element x is unique
        unique_elements.append(x)  # add the x to the unique_elements list

print(unique_elements)

"""
A list named numbers is given.
Write a program that can find unique elements of the list named numbers and return them as a new list

    Ex:
        numbers = [10, 20, 10, 30, 30, 40, 40, 40, 40, 500, 50, 50]

        Output:
            unique_elements = [20, 500]
"""
