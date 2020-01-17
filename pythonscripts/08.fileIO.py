# 在shell中读取文件可以使用cat/head/tail -> 操作文件: echo > >>
# 在Python中读取文件可以使用: open(filepath, mode=r/w/a, encoding) -> 操作文件的方法: readline/readlines/read/write

files = open("files/kingdoms.txt", "r", encoding='utf8')

# 读取全部文件内容, 读取结果为字符串
# content = files.read()
# line = content.replace("\n", "").replace(" ", "")

# 读取文件全部内容, 读取结果为列表, 每行作为列表中的元素
# alllines = files.readlines()
# print(alllines)

# 类似于生成器, 每次调用时读取文件的一行内容, 下次读取从上次的下一行读取
# n = 10
# while n >= 0:
#     print(files.readline())
#     n -= 1

# # 统计青龙偃月刀的出现次数
# print(line.count("丞相"))

files.close()

wfile = open("files/wfile.txt", "a", encoding="utf8")

wfile.write(
    """
    hello everyone:
        nice to meet you
        nice ti meet you too
        append...
    """
)

wfile.close()


with open("files/wfile.txt", "r", encoding="utf8") as files:
    print(files.read())

