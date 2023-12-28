password = input("Enter the password:")
result = {}
# check len of password
if len(password) > 8:
    result["length"] = True
else:
    result["length"] = True

# check isDigit present
digit=False
for i in password:
    if i.isdigit():
        digit=True
result["digit"] = digit


# check Capital
upperCase = False
for i in password:
    if i.isupper():
        upperCase=True
result["upper-case"] = upperCase

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Week password")



