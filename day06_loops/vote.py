age = int(input('Enter your age:\n'))

while age < 0 or age > 150: # while the user enters invalid age
    age = int(input('Invalid age! Please re-enter your age:\n'))

us_citizen = input('Are you are us citizen?\n')

while not (us_citizen.lower() == 'yes' or us_citizen.lower() == 'no'): # while the user enter invalid answer
    us_citizen = input('Invalid answer! Please re-enter, are you are us citizen?\n')

if age >= 18 and us_citizen.lower() == 'yes':
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')