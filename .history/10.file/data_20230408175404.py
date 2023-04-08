# # 存储数据到json

# import json

# number = [2,3,4,5,6]

# filename = '10.file/number.json'
# with open(filename,'w') as file_obj:
#   json.dump(number,file_obj)


# # 从json读取数据
# import json

# filename = '10.file/number.json'
# with open(filename) as file_obj:
#   numbers = json.load(file_obj)

# print(numbers)

# # 把用户数据保存到json
# import json

# username = input("place enter your name")

# filename = '10.file/username.json'
# with open(filename,'w') as file_obj:
#   json.dump(username,file_obj)
#   print("We'll remember you when you come back, " + username + "!")

# 从json中读取用户数据
import json

filename = '10.file/username.json'
with open(filename) as file_obj:
  username = json.load(file_obj)
  print("We'll remember you when you come back, " + username + "!")

