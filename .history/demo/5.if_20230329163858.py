
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
# in
cars= ['a','b','c']
if 'bmw' in cars:
    print('bmw在cars中')
# not in
if 'bmw' not in cars:
    print('bmw不在cars中')

#if-else
if car == 'bmw':
    print('True')
else:
    print('False')

# 列表是否为空
list = []
if list:
    print('列表不为空')
else:
    print('列表为空')


big_list=['a','b','c']
small_list=['a','b']