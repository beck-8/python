
# 1到100内既能被3整除，又能被2整除的数字
# for i in range(1,100):
#     if i%3==0 and i%2==0:
#         print(i)


# 根据输入的成绩进行打分, 学习成绩>=90分的同学用A表示;60-89分之间的用B表示;60分以下的用C表示;
# cj=int(input("Please input grade:"))
# if cj >=90:
#     print("A")
# elif cj >=60 and cj <=90:
#     print("B")
# else :
#     print("C")


# 思考题: 计算2-3+4-5+6-7+8-9 …. +98-99+100的结果
# n,m=0,0
# for number in range(2,101):
#     if number % 2 == 0:
#         n += number
#     else:
#         m += number
# print(n-m)

# s,n=0,2
# while n<=100:
#     s += n*(-1)**n
#     n += 1
# print(s)

# 请问这个长阶梯有多少阶？(200以内)
# for i in range(7,201,7):
#     if i%2==1 and i%3==2 and i%5==4 and i%6==5 and i%7==0:
#         print(i)
i=7
while i <=200:
    if i%2==1 and i%3==2 and i%5==4 and i%6==5 and i%7==0:
        print(i)
    i += 1
