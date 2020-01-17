# python基本的数据类型: int, float, str, bool
# python基本的数据结构: 元组tuple, 列表list, 字典dict, 集合set
# tuple元组: 增删改查

# 元组的声明方式
tuple01 = (1, 2, 3.14, "hello world", False)
print(tuple01, type(tuple01))

list01 = [1, 2, 3, 4]
print(list01, type(list01))

# 元组与列表的转换
tuple02 = tuple(list01)
print(tuple02, type(tuple02))

list02 = list(tuple01)
print(list02, type(list02))

# 对于元组的遍历
for index in range(len(tuple01)):
    print(tuple01[index])

for element in tuple01:
    print(element)

# 元组的切片-> 支持索引号
str01, tuple01 = "hello world", (1, 2, 3.14, "hello world", False)
#          0  1   2      3            4
#         -5 -4  -3     -2           -1
# -> 求元组的长度
print(len(tuple01))

print(tuple01[1:4])
print(str01[1:4])

# 元组自带的方法
tuple03 = (1, 2, 3, 2, 2, 6, 2)
print(tuple03)
# -> index方法找到所传字符的索引号
indexs = tuple03.index(2)
print(indexs)
# -> count方法统计指定字符在元组中的数量
number = tuple03.count(2)
print(number)

# 元组是一个不可改变的数据结构
# tuple03[3] = 4
# print(tuple03)
# 若想改变元组中的数据,可利用源元组搭配其他数据, 进行修改, 返回新数据到新的元组中;
tuple04 = (1, 2, 3)
tuple05 = (2, 3, 4)
tuple06 = tuple04 + tuple05[2:]
print(tuple06 * 3)
