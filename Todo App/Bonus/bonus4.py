filename = ['1.Raw Data.txt', '2.Reports.txt', '3.presentation.txt']

for file in filename:
    file = file.replace('.', '_',1)
    print(file)