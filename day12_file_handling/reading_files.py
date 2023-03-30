# open(path, mode)
text_file1 = open('/Users/cydeo/PycharmProjects/Python_Programming/day12_file_handling/ReadTextFile1.txt', 'r')

texts = text_file1.read()

print(texts)

text_file1.close()


print("-------------------------------------------------------------------------------")

text_file1 = open('/Users/cydeo/PycharmProjects/Python_Programming/day12_file_handling/ReadTextFile1.txt', 'r')

text1 = text_file1.readline()
text2 = text_file1.readline()

print(text1)
print(text2)

text_file1.close()

print("-------------------------------------------------------------------------------")

text_file2 = open('/Users/cydeo/PycharmProjects/Python_Programming/day12_file_handling/ReadTextFile2.txt', 'r')

print(text_file2.read())

text_file2.close()

print("-------------------------------------------------------------------------------")

text_file2 = open('/Users/cydeo/PycharmProjects/Python_Programming/day12_file_handling/ReadTextFile2.txt', 'r')

print(text_file2.readline())
print(text_file2.readline())
print(text_file2.readline())








