# 字典
alien = { 'name':'xxx','age':18}
# 格式化字典
alien = { 
    'name':'xxx',
    'age':18,
    }


# 访问字典中的值
print(alien['name'])

# 修改字典中的值
alien['age'] = 19
print(alien['age'])

# 添加键值对
alien['color'] = 'red'
print(alien)

# 删除键值对
del alien['color']
print(alien)


# items()方法
print(alien.items())
# keys()方法
print(alien.keys())
# values()方法
print(alien.values())
# get()方法
print(alien.get('name'))

# 遍历字典
for key,value in alien.items():
    print(key,value)

# 排序key
for key in sorted(alien.keys()):
    print(key)


#set 集合 去重
lang = ['aaa','aaa','bbb','ccc']
print(set(lang))
# 结果排序变化
# {'ccc', 'bbb', 'aaa'}


# 嵌套
aliens = [
    {'color':'green','points':5},
    {'color':'green','points':5},
    {'color':'green','points':5},
          ]