content=["This is first file conetnt",
         "This is first second conetnt",
         "This is first third conetnt"]

filename = ['1.txt', '2.txt', '3.txt']

for content, filename in zip(content, filename):
    file = open(f"../file/{filename}", 'w')
    file.write(content)