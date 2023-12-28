'''
The true meaning of obscurity lies underneath the most delicate structures of viscosity.
The idea of changing that balance is obscure by itself.

Write a program that reads the essay.txt file and returns the number of characters contained in the file.
'''


file = open('../file/testing.txt', 'r')
sentence = file.readline()
print(len(sentence))


