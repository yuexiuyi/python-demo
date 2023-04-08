
# 区分大小写
# == 是否相等
car = 'bmw'
print(car == 'bmw')
# == 是否不相等
print(car != 'bmw')
 
# if
if car == 'bmw':
    print('True')

# 比较数字, >, <, >=, <=
age = 18
if age<18:
    print('未成年')

# and
if age<18 and age>10:
    print('10-18')
# or
if age>18 or age<10:
    print('大于18或小于10')
# not
if not age<18:
    print('大于18')