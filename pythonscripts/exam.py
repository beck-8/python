# 函数的声明
def fname(param01=None, param02=None):
    result = param01 + param02
    return result


# 函数的调用
variable = fname(param01=12, param02=13)
print(variable)


# 变量作用域
variable = "global"
def changed():
    global variable
    variable = "local"
    return variable


print(changed())
print(variable)

def waibu(x=0):
    def neibu():
        nonlocal x
        x += 1
        return x
    return neibu()


result = waibu(4)
print(result)


# 闭包: 在全局调用内部函数的机制
def sqrts(sqrt=1):
    def wrapper(number=0):
        return number ** sqrt
    return wrapper


jsq = sqrts(sqrt=2)   # jsq = wrapper() = number ** sqrt
print(jsq(2))
print(jsq(4))


number = [x for x in range(1000)]
print(number)


dictA = {"key1": 1, "key2": 2, "key3": 3}


