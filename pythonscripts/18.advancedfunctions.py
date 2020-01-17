# map(functions's name, iterable)

# def sqrts(number):
#     return number ** 2


listA = [1, 2, 3, 4, 5, 6]
# listB = []
# for element in listA:
#     listB.append(sqrts(element))
# print(listB)
sqrt = lambda number: number ** 2
list_sqrts = map(sqrt, listA)
print(list(list_sqrts))


# filter()
def residual(number):
    if number % 2 == 0:
        return number


result = filter(residual, range(10))
print(list(result))
result = map(residual, range(10))
print(list(result))


# reduce()
from functools import reduce

# def nick(a, b):
#     return a + b


nick = lambda a, b: a + b
result = reduce(nick, range(101))
print(result)


# nick functions
def add(a=0, b=0):
    return a + b


qiuhe = lambda a, b: a + b

print(add(13, 2))
print(qiuhe(13, 2))

# sorted()排序
ips = {'1.1.1.1': 12, '2.2.2.2': 43, '3.3.3.3': 11, '4.4.4.4': 76, '5.5.5.5': 16}
ips_sort = sorted(ips.items(), key=lambda x: x[1], reverse=True)
print(dict(ips_sort))
