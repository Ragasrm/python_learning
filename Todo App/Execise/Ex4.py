fileName = ['1.doc', '1.ragav', '1.hemath']

new_fileName = [file.replace('.', '-') + '.txt' for file in fileName]
print(new_fileName)