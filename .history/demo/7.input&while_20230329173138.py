# Input 获取用户输入
name = input('Please enter your name: ')
print('Hello, ' + name + '!')

# While 循环

prompt = "\nPlease enter your name: "
prompt += "\nEnter 'quit' to end the program. "
while True:
    print(prompt)
    name = input()
    if name == '':
        break