# var01 = int(input("word01: "))
# var02 = int(input("word02: "))
# var03 = int(input("word03: "))
#
# list01 = [var01, var02, var03]
#
# maxNum = list01[0]
# for element in list01:
#     if maxNum < element:
#         maxNum, element = element, maxNum
# print(maxNum)



def opera(*args):
    listA = list(args)
    maxn = listA[0]
    for element in listA:
        if maxn < element:
            maxn, element = element, maxn
    return maxn


result = opera(2000, 3000, 4000)
print(result)


# 函数的嵌套
def Accumulate(number=0):
    if type(number) not in {str, int}:
        response = 'Please Check Your Input!!!'
        return response  # 当函数遇到return直接结束,不再继续运行;

    def opera(number):
        result = 0
        for n in range(number + 1):
            result += n
        return result

    return opera(number)


result = Accumulate(5)
print(result)
