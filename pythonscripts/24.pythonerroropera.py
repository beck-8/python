# 异常: 就是在程序中未发现语法错误, 但是程序执行起来后, 被逻辑上的错误阻断执行
# 错误: 在Python中, 不符合语法规则的编码就叫做错误
# 错误处理框架: try ... except ... finally ...

# try:
#     print(10 / 0)
# except ZeroDivisionError as error:
#     print("except info: {}".format(error))
# finally:
#     print("end")
#
# print("go on. . .")
#
# try:
#     order * 2
# except NameError as error:
#     print(error)
# finally:
#     print("end")
#
# print("go on . . .")
#
# try:
#     print(1 + [1, 2])
# except TypeError as error:
#     print(error)
# finally:
#     print("end")
#
# print("go on . . .")


try:
    string = "hello world"
    # print(string[len(string) + 1])
    index = int(input("index number: "))
    if index < 0 or index >= len(string):
        raise IndexError("this index out of range")
    else:
        print(string[index])
except IndexError as error:
    print(error)

print("go on . . .")




