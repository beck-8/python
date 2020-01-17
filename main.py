# 不用重复的造轮子
from logAnlysis.zibao import jiafa
import os


def adds(a, b):
    return a + b


result = jiafa.add(12, 13)
print(result)

result = jiafa.println("string", "string01", "string02")
print(result)
