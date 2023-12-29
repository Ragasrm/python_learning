def get_average():
    with open('file/data.txt', 'r') as file:
        data = file.readlines()
    value = [float(i) for i in data[1:]]
    return sum(value) / len(value)
    
    
average = get_average() 
print(average)