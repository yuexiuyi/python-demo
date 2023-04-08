# 字典
alien = { 'name':'xxx','age':18}
# 格式化输出
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
