# # Input 获取用户输入
name = input('Please enter your name: ')
print('Hello, ' + name + '!')

# While 循环

prompt = "\nPlease enter your name: "
prompt += "\nEnter 'quit' to end the program. "
while True:
    print(prompt)
    name = input()
    if name == 'quit':
        break
    print('Hello, ' + name + '!')
    


# 把用户输入添加到字典中
users =[]
while True:
    name = input('Please enter your name:')
    age = input('Please enter your age: ')
    users.append({'name': name, 'age': age})
    repeat = input('"Would you like to let another person respond? (yes/ no)')

    if repeat == 'no' :
        break
print(users)