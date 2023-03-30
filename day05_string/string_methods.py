#  lower(): returns the lower case version of the String
s = 'CYDEO SCHOOL'
s = s.lower()  # 'cydeo school'

print(s)

#  upper(): returns the upper case version of the String
s = 'wooden spoon'
s = s.upper()  # 'WOODEN SPOON'

print(s)

#  capitalize(): returns the capitalized (first character converted to uppercase) version of the String
s = 'python PROGRAMMING LANGUAGE'
s = s.capitalize()  # 'Python programming language'

print(s)

#  title(): returns new String by converting each word's first character to upper case
s = 'python proGramming lanGuage'
s = s.title()

print(s)

#  strip(): returns new String by removing all the white spaces at both starting and ending of the string
s = '            python            '
s = s.strip().capitalize()  # 'Python'
print(s)

#  lstrip(): returns new string by removing all the white spaces at the starting of the String
s = '              CYDEO             '
s = s.lstrip().capitalize()  # 'Cydeo             '

print(s)

#  rstrip(): returns new String by removing all the white spaces at the ending of the String
s = '             Wooden Spoon          '
s = s.rstrip()  # '             Wooden Spoon'

print(s)

#  index(): returns the index number of first occurrence of the given value
s = 'Play I love Python Play'
a = s.index('Py')

print(a)

#  rindex(): returns the index number of last occurrence of the given value
s = 'Play I love Python Play'
b = s.rindex('P')

print(b)

#  replace(old_val, new_val): returns new String by replacing all the matching value with the new value
s = 'I love Java, Java is the best programming language'
s = s.replace('Java', 'Python')

print(s)

#  count(str): returns the frequency of the given value from the String
s = 'Python Python Python Java Java Java python PyThON jaVA java'

count_java = s.count('Java')
count_python = s.lower().count('python')

print(count_python)
print(count_java)

#  swapcase(): returns new string by swapping all lower/upper case characters to upper/lower cases
s = 'PYTHON programming'
s = s.swapcase()

print(s)

#  startswith(str): checks if the String starts with the given value, returns boolean
s = 'Python is the best'

r1 = s.lower().startswith('python')
r2 = s.startswith('Java')

print(r1)
print(r2)

#  endswith(str): checks if the String ends with the given value, returns boolean
s = 'cydeo@gmail.com'

gmail_address = s.endswith('@gmail.com')
yahoo_address = s.endswith('@yahoo.com')

print(gmail_address)
print(yahoo_address)

#  islower(): checks if all the characters of the string are lower case letters, returns boolean
s = 'hello world'

print(s.islower())


#  isupper(): checks if all the characters of the string are upper case letters, returns boolean
s = 'HELLO WORLD'
print(s.isupper())


#  isdigit(): checks if all the characters of the string are digits, returns boolean
s = '123'

print(s.isdigit())


#  isalpha(): checks if all the characters of the string are letters, returns boolean
s = 'abcABC'

print(s.isalpha())


#  istitle(): checks if each word starts with uppercase letter, returns boolean
s = 'Cydeo School'

print( s.istitle() )
