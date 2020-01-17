# 函数作用域

# 全局变量: 在函数中可以调用全局变量
variable = "hello world"

def add():
    return variable + " " + "kitty"


print(add())
print(variable)

# 全局变量: 全局变量与局部变量
variable = "hello world"

def adds():
    global variable
    variable = "hello kitty"
    return variable


print(adds())
print(variable)


# 局部变量: 函数嵌套的函数中的变量

def waibu(x):
    def neibu():
        nonlocal x
        x += 1
        return x
    return neibu()


print(waibu(5))
