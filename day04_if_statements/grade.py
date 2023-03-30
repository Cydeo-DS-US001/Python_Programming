score = -20

grade = None

if 0 <= score <= 100:

    if 90 <= score:  # false: score < 90
        grade = 'A'
    elif 80 <= score:  # false: score < 80
        grade = 'B'
    elif 70 <= score:
        grade = 'C'
    elif 60 <= score:
        grade = 'D'
    else:
        grade = 'F'
else:
    grade = 'Invalid'

print(grade)
