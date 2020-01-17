# 循环框架(for while)
# range: 生成器-可有用户指定范围生成该范围内的整数, 范围的规定为左闭右开区间
# 使用for打印出1~100 -> 左闭右开区间 [1, 101) -> 不等式: 1 =< x > 101
for i in range(100):
    print(i)

# 查找出100以内所有的偶数
for i in range(1, 101):
    if i % 2 == 0:
        print(i)


# 使用while打印1~100
n = 1
while n < 101:
    print(n)
    n += 1

# 查找出1~100中所有的奇数
n = 100
while n > 0:
    if n % 2 == 1:
        print(n)
    n -= 1


# - 若每步上2阶,最后剩下1阶;
# - 若每步上3阶,最后剩2阶;
# - 若每步上5阶,最后剩下4阶;
# - 若每步上6阶,最后剩5阶;
# - 只有每步上7阶, 最后刚好一阶也不剩
# 请问这个长阶梯有多少阶？(200以内)
ladds = 7
while True:
    if ladds % 2 == 1 and ladds % 3 == 2 and ladds % 5 == 4 and ladds % 6 == 5 and ladds % 7 == 0:
        print(ladds)
        break   # 终止
    ladds += 7


for ladds in range(7, 201, 7):
    if ladds % 2 == 1 and ladds % 3 == 2 and ladds % 5 == 4 and ladds % 6 == 5 and ladds % 7 == 0:
        print(ladds)


# continue中止循环继续下一次循环;
for i in range(100):
    if i % 2 == 0:
        continue
    print(i)


# 2-3+4-5+6-7....+98-99+100 求和;
n, m = 0, 0
for number in range(2, 101):
    if number % 2 == 0:
        n += number
    else:
        m += number
print(n - m)


s, n = 0, 2
while n <= 100:
    s += n * (-1)**n
    n += 1
print(s)


