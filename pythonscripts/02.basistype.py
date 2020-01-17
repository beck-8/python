# python中基本的数据类型: 整型, 浮点型, 字符串类型, 布尔值类型
#
# 整型(int): 0 1 2 3 4 5 ..... (-1, -2, -3 .....)
# 浮点数(float): 3.14 4.445 0.414 5.4132465465 .....
# 字符串类型(str): 有<单引>或<双引>或<三引>括起来的字符都叫做字符串类型的数据;
# 布尔值类型(bool): 专指True或False, 特殊情况下True被识别为1,False被识别为0;


var01, var02, var03, var04 = -18, -4.445, "string", False
print("var01's type: ", type(var01))
print("var02's type: ", type(var02))
print("var03's type: ", type(var03))
print("var04's type: ", type(var04))


# 整型及浮点型的运算
# -> 加法:
print(var01 + var02)
var05 = var01 + var02
print(var05)

# -> 减法:
print(var01 - var02)

# -> 乘法:
print(var01 * 3)

# -> 除法:
var06 = var01 / 2
print("result: ", var06, "var06's type: ", type(var06))

# -> 取余:
print(var01 % 5)

# -> 整除:
print(var01 // 5)

# -> 比较运算符-> 大于/小于/大小等于 -> 比较运算符会产生布尔值类型的数据,用于if判断;
print("var01 > var02 result: ", var01 > var02)

# -> 逻辑运算符
print("True and False: ", True or False)
print("not True: ", not True)


# 数据类型的转换(重点) int() float() str() bool()
# -> 整型转换为浮点型
var07 = 0
print(var07, type(var07))

var07 = float(var07)
print(var07, type(var07))

var07 = str(var07)
print(var07, type(var07))

var07 = bool(var07)
print(var07, type(var07))

var08 = "a"
print(var08, type(var08))

var08 = bool(var08)
print(var08, type(var08))


