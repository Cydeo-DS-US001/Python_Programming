s = "CYDEO"

print(len(s))  # total number of characters

# Forward indexes: 0, 1, 2, 3, 4
# reverse indexes: -1, -2, -3, -4, -5

last_forward_index = len(s) - 1  # 4

print(s[0])

print(s[-1])
print(s[-2])

print(s[len(s) - 1])
print(s[len(s) - 2])

print("-----------------------------------------------------------")

s = 'Python Programming Language'

word1 = s[7:18]  # index 18 is excluded

print(s)
print(word1)

sentence = 'I love Python Programming'

word2 = sentence[7:13]

print(word2)

a = 'Python Programming Language'

word3 = a[:18]  # by default, slicing starts from index 0

print(word3)

b = 'CYDEO School'

word4 = b[:5]

print(word4)

name = 'Wooden Spoon'
result = name[::-1]
print(result)

s = 'I love Python programming language'

word5 = s[14:]

print(word5)

sentence = 'Today is Friday'

word6 = sentence[9:]

print(word6)
