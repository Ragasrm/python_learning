import glob

myfiles = glob.glob("file/*.txt")

for filePath in myfiles:
    with open(filePath, 'r') as fileContent:
        print(fileContent.read())
        

print(myfiles)