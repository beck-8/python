import random


print(random.random())					# 随机产生一个0到1之间的小数

print(random.uniform(0, 9))			# 随机产生一个0到9之间的小数

print(random.randint(1, 9))     # 随机输出一个1到9之间的整数

element = [1, 2, 3, [4, 5, 6], 'ABC', 'employee']
print(random.choice(element))   # 随机输出列表中的某个元素

number = [1, 2, 34, 57, 81, 99]
random.shuffle(number)          # 打乱给定列表中的元素
print(number)

# list:
listA = [1, 3, 2]
listB = [3, 2, 1]

print(listA is listB)
print(listA == listB)

random.shuffle(listA)
print(listA)
print(listB)
print(listA == listB)


# 模拟验证码
def vcode(number=4):
    c = ""
    for i in range(number):
        nums = random.randint(0, 9)
        word = chr(random.randint(65, 90))
        middle = random.choice([nums, word])
        c += str(middle)
    return c


codes = vcode(6)
print("请输入验证码: {}".format(codes))
people_input = input("input: ")
if codes == people_input.upper():
    print("successfully")
else:
    print("failed")







