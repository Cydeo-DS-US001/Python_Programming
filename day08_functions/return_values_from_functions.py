def square(num):
    result = num * num
    return result


n = square(20)

print(n)

print(square(100))


def cube(num):
    result = square(num) * num
    return result


m = cube(20)

print(m)

print('-----------------------------------------------------------------------')


def grade(score):
    result = None
    if 0 <= score <= 100:  # score is valid

        if score >= 90:
            result = 'A'
        elif score >= 80:
            result = 'B'
        elif score >= 70:
            result = 'C'
        elif score >= 60:
            result = 'D'
        else:
            result = 'F'

    else:  # score is invalid
        result = 'Invalid score'

    return result


grade = grade(85)

print(grade)

if grade == 'A':
    print('Excellent')
elif grade == 'B':
    print('Great')
elif grade == 'C':
    print('Good')
elif grade == 'D':
    print('Passed')
else:
    print('Failed')

print('-----------------------------------------------------------------------')


def multiply(a, b):
    return a * b


def calc_rectangle_area(width, length):
    return multiply(width, length)



width = 15
length = 20

x = calc_rectangle_area(width, length)

print(x)









