# shell's function:
# function fname() {
#     functions
# }

# 调用 fname

# python's function:
def add():
    a, b = 12, 13
    print(a + b)


# python函数的调用
add()

# 用过的函数
# type()
# print()
# len()
# open()
#
# int()
# float()
# bool()
# str()
# list()
#   -> sort(reverse=True)
# tuple()
# dict()
# set()


# 函数的参数
def adds(a, b):
    print(a + b)


# 调用函数
# adds(a=12, b=13)
for n in range(1, 10):
    adds(a=12, b=n)

adds(12, 13)
# adds(a=12, 13)
adds(12, b=13)
# open(file='12.functionopera.py', 'r', encoding='utf8')
# adds(12)

# 函数的参数 之  默认参数
def addss(a=0, b=0):
    print("a is: {}".format(a))
    print("b is: {}".format(b))
    print("a + b = {}".format(a+b))


# 只传a
addss(a=12)
addss(12)
# 只传b
addss(b=13)

# print()功能实现
print(1, 2, "world")

def println(*args):
    print(args, type(args))
    if type(args[2]) == str:
        print("hello {}".format(args[2]))
    else:
        print("args[2]'s type is not str")


println(1, 2, "world", 4)


def printf(**kwargs):
    """:arg: (1)name, (2)age, (3)sex"""
    print(kwargs, type(kwargs))
    for items in kwargs.items():
        if items[0] == "sex":
            print(items[1])


printf(name='tom', age=18, sex="MAN")
# help(printf)

# 不限制参数的长度, 也不限制参数的类型
def example(*args, **kwargs):
    pass

# 函数的返回值
def add(a, b):
    return a + b


result = add(12, 13)
print(result)
