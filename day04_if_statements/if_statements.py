age = 21

if age >= 21:
    print('You are eligible to buy alcohol')

print("---------------------------------------------------")

score = 55

if score >= 60 :  # False
    print('Congrats, You passed the exam!')

if score < 60 :  # True
    print('You failed the exam')

print("---------------------------------------------------")

if score >= 60 : # Passed
    print('Congrats, You passed the exam!')
else : # Failed
    print('You failed the exam')

print("---------------------------------------------------")

age = int(input('Enter your age:\n'))

if age >= 21 :
    print("Eligible")
else :
    print("Not Eligible")
