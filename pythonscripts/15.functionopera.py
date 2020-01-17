# 闭包: 在全局中调用内部函数的机制
# 做一个求平方的函数
# def sqrt(number=0):
#     return number ** 2

def sqrts(sqrt=3):
    def wrapper(number=0):
        return number ** sqrt
    return wrapper


# 生成一个计算任何数字三次方的计算器
jsq = sqrts(3)
# jsq(number=4) = wrapper(number=4)

number4 = jsq(number=4)
print(number4)


# def wrapper(number=0):
#     return number * 10
#
#
# variable = wrapper
#
# print(variable)
# print(wrapper(3))
# print(variable(3))

