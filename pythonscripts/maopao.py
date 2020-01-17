# for循环构成的冒泡排序

listA = [23, 12, 15]
for i in range(len(listA)):
    for j in range(len(listA) - 1):
        if listA[j] > listA[j+1]:
            listA[j], listA[j+1] = listA[j+1], listA[j]
print(listA)

# 循环次数为: len(listA) * (len(listA) - 1)

# i = 0
# -> j = 0 -> if listA[0]=23 > listA[0+1]=12 -> 交换
# result: [12, 23, 15]
# -> j = 1 -> if listA[1]=23 > listA[1+1]=15 -> 交换
# result: [12, 15, 23]


# 1.将句子"this is my house" 反转为 "house my is this"
change, sentence = "", "this is my house"
sentence_split = sentence.split()
sentence_split.reverse()
for element in sentence_split:
    change = change + element + ' '
print(change.rstrip())

# 字符串中自带的方法有 join()
sentence = "this is my house"
print(' '.join(sentence.split()[::-1]))

# ass = [1, 2, 3, 4]如何进行方向输出
ass = [1, 2, 3, 4]
for i in ass[::-1]:
    print(i)


# 2. 敏感字符替换, 如句子中存在有特殊的敏感词汇,直接把敏感词汇替换成"*"号
search = input("please input content: ")
new_search = search.replace("苍老师", "*老师").replace("王亚刚", "***")
print("你搜索的关键字为: {}".format(new_search.split()))

# 3. 现在有这样一个元组("string", "world", 1, 2, 3, 4, 6, 9, 10), 把其中的数字提取到一个列表中
listA, tupleA = [], ("string", "world", 1, 2, 3, 4, 6, 9, 10, 3.14, 4.445, 78, 99, 100)
for element in tupleA:
    if type(element) in (int, float):
        listA.append(element)
print(listA)

# 4. list01 = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]转换成["string", "tuple", "list", 1, 2, 3, 4, 5, 6, 7]
listB, listC = [], ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
# for element in listB:
#     if type(element) in (list, tuple):
#         for e in element:
#             listB.append(e)
#         listB.remove(element)
# print(listB)

# for index in range(len(listB)):
#     if type(listB[index]) in (list, tuple):
#         for element in listB[index]:
#             listB.insert(index, element)
#         listB.pop(index)
# print(listB)

for element in listC:
    if type(element) not in (int, float, str, bool):
        for e in element:
            listB.append(e)
    else:
        listB.append(element)
print(listB)

# 5. 对[23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]进行排序, 要求使用for循环
listD = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
listD.sort(reverse=True)
print(listD)
