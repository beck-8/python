# 声明集合
setA = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
listA = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(setA)
print(listA)

listA = list(set(listA))
print(listA)
# 总结: 集合是天然的去重工具

# element = []
# for i in listA:
#     if i in element:
#         listA.remove(i)
#     else:
#         element.append(i)
# listA = element
# del element
# print(listA)


#  -> 交并集
set01 = {2, 1, 4, 3}
set02 = {3, 4, 5, 6}


# -> 交集
set03 = set01 & set02
print(set03)
# -> 并集
set04 = set01 | set02
print(set04)


# 成员判断符
if "3" in set04:
    print("exists")
else:
    print("not exists")

# 集合是不是可迭代对象
for i in set04:
    print(i)

# 集合的增删查
print(set04)

# -> 增加元素
set04.add("string")
print(set04)

set04.update([7, 8, 9])
print(set04)
# 集合是无序的

# -> 删除元素
# set04.clear()
# print(set04)

set04.remove(9)
print(set04)

# set04.pop()
# print(set04)

# set -> list -> list's function -> set


