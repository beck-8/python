# 字符串

# 字符串的声明
string01 = 'hello \nworld'
string02 = "hello \nworld"
string03 = '''
hello world
hello kitty
hello tom'''
string04 = """
hello world
hello kkkkk
hello ttttt"""

print(string01)
print(string02)
print(string03)
print(string04)

# sentence = "this's my\" house"


# 字符串的切片
sentence = "python is good language"
# p    y  t  h  o  n     i  s     g  o  o  d     l  a  n  g  u  a  g  e
# 0    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22
# -23 -22 -21   ......          ....            .....       ....   -2 -1
print(sentence[0])
print(len(sentence))
print(sentence[len(sentence)-1])

# -> 遍历字符串
for index in range(len(sentence)):
    print(sentence[index])

# -> 字符串是可迭代对象
for element in sentence:
    print(element)

# -> 字符串切片
print(sentence[0:6])
print(sentence[7:])
print(sentence[:7])
print(sentence[:])
print(sentence[-1])
print(sentence[0:-1])


# 字符串自带的方法
string = "hello world"

# 字符串的切片方法
string_split = string.split("o")
print(string)
print(string_split)

# 字符串的替换
string_replace = string.replace("o", "0", 3)
print(string)
print(string_replace)

# 字符串的加法-> 拼接
new_string = string + " " + "abc123"
print(new_string)

# 字符串的乘法-> 重复输出
print(string * 4)
print("---" * 20)

# 字符串去除首尾字符
var01 = "as   hello world  sa"
print(var01)
var01_strip = var01.strip("s")
print(var01_strip)
var01_rstrip = var01.rstrip("s")
print(var01_rstrip)
var01_lstrip = var01.lstrip("a")
print(var01_lstrip)

# 字符串的格式化
print("var01's type: ", type(var01))
print("var01's value: ", var01, "var01's type: ", type(var01))
print("var01's type: {}".format(type(var01)))
print("var01's values: {}; var01's type: {}".format(var01, type(var01)))

float01, float02 = 4.4456789, 0.123
print("对float01保留两位小数: {:.2f}".format(float01))

print("wz1: {1}, wz2: {0}".format(float02, float01))


# 成员判断符
print("s" in "hello")

var02, var03 = "ss", "hello world"
if var02 not in var03:
    print("var03 include var02")
else:
    print("var02 not include var03")
