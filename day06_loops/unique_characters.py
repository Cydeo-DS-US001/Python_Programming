str = 'aaabccccdeeeeeeef'
unique = ""

for x in str:  # x: each character
    if str.count(x) == 1: # bif the character's frequency is 1, then it's unique
        unique += x

print(unique)