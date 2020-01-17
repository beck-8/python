# 条件判断
#
# if条件判断
var01 = int(input("please input var01: "))
if var01 > 0:
    print("var01 > 0")
else:
    print("var01 = 0 or var01 < 0")

# 独立条件判断
var02 = int(input("please input var02: "))
if var02 < 0:
    print("var02 < 0")
elif var02 < 10:
    print("var02 < 10")
elif var02 < 20:
    print("var02 < 20")
else:
    print("var02 > 20 or var02 = 20")

# if嵌套结构 -> 多条件判断
var03 = int(input("please input var03: "))
if var03 % 2 == 0:
    if var03 % 3 == 0:
        print("var03对2以及3都可以整除")
    else:
        print("var03只能对2整除,不能对3整除")
else:
    if var03 % 3 == 0:
        print("var03只能对3整除不能对2整除")
    else:
        print("var03对2或3都不能整除")

# 多条件判断框架
var04 = int(input("please input var04: "))
if var04 % 2 == 0 and var04 % 3 == 0:
    print("var04对2以及3都可以整除")
elif var04 % 2 == 0 and var04 % 3 != 0:
    print("var04只能对2整除,不能对3整除")
elif var04 % 2 != 0 and var04 % 3 == 0:
    print("var04只能对3整除不能对2整除")
else:
    print("var04对2或3都不能整除")
