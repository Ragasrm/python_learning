names = ["john smith", "jay santi", "eva kuki"]
new_name = [ name.title() for name in names]
print(new_name)

usernames = ["john 1990", "alberta1970", "magnola2000"]
number_of_char = [ len(name) for name in usernames]
print(number_of_char)

user_entries = ['10', '19.1', '20']

sum = sum([float(add) for add in user_entries])
print(sum)

