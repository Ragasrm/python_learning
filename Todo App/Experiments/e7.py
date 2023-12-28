file = open('../file/members.txt', 'r')
user_name = file.readlines()
file.close()

user_added_name = input("Enter the user name:")
user_name.append(user_added_name)

file = open('../file/members.txt', 'w')
file.writelines(user_name)
file.close()