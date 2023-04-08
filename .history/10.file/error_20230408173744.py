# # 处理异常
# try:
#   print(5/0)
# except ZeroDivisionError:
#   print ("you can not divide by zero!")

# # 使用异常避免崩溃
# print("Give me two numbers, and I'll divide them")
# print("Enter 'q' to quit")

# while True:
#       first_number = input("\nFirst number:")
#       if(first_number == 'q'):
#         break
#       second_number = input ("Second number:")
#       if(first_number == 'q'):
#         break
#       try:
#         answer = int(first_number) /int(second_number)
#       except ZeroDivisionError:
#         print ("you can not divide by zero!")
#       else:
#         print(answer)


# # 处理文件异常
# filename = '10.file/p.txt'
# try:
#   with open(filename) as f_obj:
#     contents = f_obj.read()
# except FileNotFoundError:
#   msg = "Sorry ,the file " + filename + " dose not exist."
#   print(msg)

# # 分析文本

# filename = "10.file/note.txt"
# try:
#    with open(filename) as file_obj:
#     contents = file_obj.read()
# except FileNotFoundError:
#   msg = "Sorry ,the file " + filename + " dose not exist."
#   print(msg)
# else:
#   # 计算文件大致包含多少个单词
#   words = contents.split()
#   num_words = len(words)
#   print("the file " + filename + " has about " + str(num_words) + " words")

# 分析文本抽象为方法

try:
   with open(filename) as file_obj:
    contents = file_obj.read()
except FileNotFoundError:
  msg = "Sorry ,the file " + filename + " dose not exist."
  print(msg)
else:
  # 计算文件大致包含多少个单词
  words = contents.split()
  num_words = len(words)
  print("the file " + filename + " has about " + str(num_words) + " words")
