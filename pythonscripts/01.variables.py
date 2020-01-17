#!/usr/bin/env python3
# coding: utf-8
#
# usage: study variable


# 变量的定义: 变量是一个名字, 该名字链接到内存地址; 在该地址中存储着, 该变量所代表的的值;
variable = "hello world"
print(variable)

# 变量的赋值方式(单变量, 多变量, 从键盘读取)
var01 = "hello world"               # 单变量赋值
var02, var03 = "hello", "world"     # 多变量赋值
var04 = var05 = "hello world"       # 链式赋值
var06 = input("please input: ")     # 从键盘读取
print("var01: ", var01)
print("var02: ", var02)
print("var03: ", var03)
print("var04: ", var04)
print("var05: ", var05)
print("var06: ", var06)

# 变量值的交换
n01 = "123"
n02 = "abc"
print(n01, n02)
n01, n02 = n02, n01
print(n01, n02)


