'''
The true meaning of obscurity lies underneath the most delicate structures of viscosity.
The idea of changing that balance is obscure by itself.


Take a look at the essay.txt file tab. That file contains some text.

You should create a program that reads the essay.txt file, converts the first letter of each word
to uppercase and prints out the converted text.
'''

new_sentence = ''
file = open('../file/testing.txt', 'r')
sentence = file.readline()
print(file.readline())
for word in sentence.split():
    new_sentence += " " + word.capitalize()
print(new_sentence)
