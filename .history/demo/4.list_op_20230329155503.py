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

