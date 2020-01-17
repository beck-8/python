ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}

# 在字典中增加键值对儿
ips["4.4.4.4"] = 23
print(ips)

ips.setdefault('3.3.3.3', 43)
print(ips)

ips.setdefault('5.5.5.5')   # shell: null, None -> 空
print(ips)

ips.update([('192.168.161.10', 67), ('2.2.2.2', 444)])
print(ips)

listA = ['tom', 'jerry', 'natasha']
people = {}.fromkeys(listA)
print(people)

# 修改值
people.update([('tom', 98)])
print(people)

people['jerry'] = 45
print(people)


# 删除键值对儿
people.pop('tom')
print(people)

ips.popitem()
print(ips)

ips.clear()
print(ips)

# del ips
# print(ips)

