tuple1 = ('Java', 'Java', 'Python', 'C#', 'C#', 'C#', 'Cydeo')

for x in tuple1:  # x: each element of the tuple
    f = tuple1.count(x)  # returns the frequency of each element
    if f == 1: # if the frequency of the element is 1, then it's unique
        print(x)

"""
Write a program that can display the unique elements from the tuple
			EX:
				tuple = (10, 10, 20, 30, 30, 40,  40, 40, 50)
				output:
					20
					50
"""
