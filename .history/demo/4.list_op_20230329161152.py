cars = ['a','b','c']

# for in 循环
# 通过缩进来表示循环体,只有循环体允许缩进，不允许无意义的缩进
# 必须写冒号
for car in cars:
    print(car)

print('end')


# range() 函数
# 10是上限，不包含10
for i in range(1,10):
    print(i)

# 创建数字列表
numbers = list(range(1,10))
print(numbers)

# 创建乘方列表
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# 统计列表
nums = [1,2,3,4,5,6,7,8,9,10]
# min() max() sum()
print(min(nums))
print(max(nums))
print(sum(nums))

# 列表解析
squares = [value+1 for value in range(0,10)]
print(squares)

# 切片
players = ['a','b','c']
print(players[0:1]) 

# 未指定初始索引，从0开始
print(players[:2]) 

# 返回第二个元素到最后一个元素
print(players[1:])

# 返回倒数第二个元素到最后一个元素
print(players[-2:])

# 遍历切片
for player in players[:2]:
    print(player)


# 切片列表返回为新列表
slicePlayers = players[:2]
print(slicePlayers)

# 复制列表
copyPlayers = players[:]
copyPlayers[2] = 'd'
print(copyPlayers)
print(players)

# 直接赋值会修改原列表
copyPlayers2 = players
copyPlayers2[2] = 'd'
print(copyPlayers2)
print(players)

# 元组
# 元组是不可变的，不能修改元组的元素