# # python中的列表:
#
# # 列表的声明:
# list01 = [1, 2, 3, 3.14, 4.445, "string", True]
#
# # 列表索引
# # [1, 2, 3, 3.14, 4.445, "string", True]
# #  0  1  2   3      4       5       6
# # -7 -6 -5  -4     -3      -2      -1
# print(list01[3:5])
#
# # 利用索引可以对列表进行遍历
# for index in range(len(list01)):
#     print(list01[index])
#
# for element in list01:
#     print(element)
#
#
# # 列表的方法
# listA = [1, 2, 3, "abc"]
#
# # -> 增: 插入, 追加, 拓展
# listA.append("append")
# print(listA)
#
# listA.insert(1, "insert")
# print(listA)
#
# listB = [5, 4, 5, 6]
# # listA = listA + listB
# # print(listA)
# listA.extend(listB)
# print(listA)
#
# # -> 删: 按索引删除, 按数据删除
# listA.pop(listA.index("abc"))
# print(listA)
#
# listA.remove(5)
# listA.remove(5)
# print(listA)
#
# # listA.clear()
# # print(listA)
#
# # del listA
# # print(listA)
#
# # -> 改:
# listA[3] = 333
# print(listA)
#
# # -> 查:
# index = listA.index('append')
# print(index)
#
# count = listA.count(4)
# print(count)
#
# # -> 其他:
# listA.reverse()
# print(listA)
#
# listA = [12, 34, 52, 11, 9, 13, 24, 43]
# listA.sort()
# print(listA)
#
# listB = listA.copy()
# print(listB)
#
# # 查看一个对象的内存地址编号
# print(id(listA))
# print(id(listB))
#
# if listA is listB:
#     print("listA == listB")
# else:
#     print("listA != listB")
#
# listC = [1, 2, 3]
# listD = listC
# print(id(listC))
# print(id(listD))
#
# if listC is listD:
#     print("listC == listD")
# else:
#     print("listC != listD")

# list01 = [x, 7, 8, 9, y] = size=64
# list01 = [1, 7, 8, 9] = element's size is 16
# list01 = [x, y, 1, 7, 8, 9, x, y] = size=96
# list01 = [y, 1, 7, 8, 9, 2] = size=96


list01 = [7, 8, 9]
tuple01 = (7, 8, 9)
list01_size = list01.__sizeof__()
tuple01_size = tuple01.__sizeof__()

print("list01's size: {}".format(list01_size))
print("tuple01's size: {}".format(tuple01_size))

list01.append(1)																			# 添加单个元素到列表中
list01_size = list01.__sizeof__()											# 利用__sizeof__方法查看列表大小
print("list01's size: {}".format(list01_size))				# 格式化打印list01的大小

list01.append(2)
list01_size = list01.__sizeof__()
print("list01's size: {}".format(list01_size))

list01.append(3)
list01_size = list01.__sizeof__()
print("list01's size: {}".format(list01_size))

list01.append(4)
list01_size = list01.__sizeof__()
print("list01's size: {}".format(list01_size))

list01.append(5)
list01_size = list01.__sizeof__()
print("list01's size: {}".format(list01_size))
