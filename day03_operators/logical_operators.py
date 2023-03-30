age = 28
is_us_citizen = True

is_eligible_to_vote = age >= 18 and is_us_citizen  # both
#                       true   and   true

print(f"You are eligible to vote: {is_eligible_to_vote}")

print('------------------------------------------------------------')

grade = "F"

is_early_bird = grade == 'A' or grade == 'B'  # either
passed_the_exam = grade == 'A' or grade == 'B' or grade == 'C' or grade == 'D'

print(f"You are eligible for early birds group: {is_early_bird}")
print(passed_the_exam)

print('------------------------------------------------------------')

failed_the_exam = not passed_the_exam
#                 not false

print(failed_the_exam)

num = 100

even_number = num % 2 == 0
odd_number = not even_number

print(f"{num} is even number: {even_number}")
print(f"{num} is odd number: {odd_number}")

print(not True == False)
print(not False == True)
