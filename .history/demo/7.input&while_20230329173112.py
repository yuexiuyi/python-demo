# Input 获取用户输入
name = input('Please enter your name: ')
print('Hello, ' + name + '!')

# While 循环

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
while True:
    print('Please type your name.')
    name = input()
    if name == '':
        break