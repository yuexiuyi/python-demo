# 列表

bicycles = ['aaa','bbb','ccc','ddd'];
# -1 是最后一个元素，索引-3 返回倒数第三个列表元素，以此类推
print(bicycles[-1]);

# 添加元素
bicycles.append('eee');
print(bicycles);

# 插入元素
bicycles.insert(1,'fff')
print(bicycles);

# 删除元素
del bicycles[1];
print(bicycles);

# 删除元素并返回
popped_bicycles = bicycles.pop();
print(popped_bicycles);