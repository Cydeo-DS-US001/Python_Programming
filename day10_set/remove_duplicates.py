elements = ['Java', 'Java', 'Python', 'Python', 10, 10, 10]

non_duplicates = list()  # ['Java', 'Python']

for x in elements:
    if x not in non_duplicates:  # if the element is not included in the second list yet
        non_duplicates.append(x)  # add the element to the second list

print(non_duplicates)

"""
    list1 = [1, 1, 2, 2, 3, 3]

    Output:
        non_duplicates = [1, 2, 3]
"""
