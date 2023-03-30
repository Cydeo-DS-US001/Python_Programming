
numbers = (10, 200, 50, 40, 500, 25, -5, 30)

max_num = numbers[0]  # 500
min_num = numbers[0]  # 10

for x in numbers:  # xis the elements of tuple

    if x > max_num:  # if the element of the tuple is greater than the current max_num
        max_num = x  # replace the value of max_num with that element of the tuple

    if x < min_num:  # if the element of the tuple is smaller than the current min_num
        min_num = x  # replace the value of min_num with that element of the tuple

print(f'Maximum number is: {max_num}')
print(f'Minimum number is: {min_num}')

print("------------------------------------------------------------------------")

nums = (10, 200, 50, 40, 500, 25, -5, 30, 100, 45, -1)

max_num = max(nums)
min_num = min(nums)

print(f'Maximum number is: {max_num}')
print(f'Minimum number is: {min_num}')



"""
Write a program that can display the maximum and minimum numbers from a tuple of integers
        Ex:
            numbers = (10, 200, 50, 40, 500, 25, -5, 30)

            Output:
                Maximum number is: 500
                Minimum number is: -5

        DO NOT use the build-in functions max() & min()
"""
