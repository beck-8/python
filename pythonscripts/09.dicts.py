# 字典的声明
dictA = {"192.168.123.11": 34, "39.167.178.34": 54}
print(dictA)

dictB = dict([("192.168.123.11", 34), ("39.167.178.34", 54)])
print(dictB)

dictC = dict(classname="cloud1909", people=45)
print(dictC)


# 调用字典中键所对应的值
print(dictA["192.168.123.11"] + 1)

# 遍历字典: -> 遍历字典的key; 遍历字典的values; 遍历键值对儿;
# -> 遍历字典的key;
for keys in dictA.keys():
    print(keys)

# -> 遍历字典的values;
pv = 0
for values in dictA.values():
    pv += values
print(pv)
print(len(dictA))

# -> 遍历键值对儿;
for items in dictA.items():
    print(items)

# 思考题: 根据访问次数排序:
# ips = {
#           "192.168.123.11": 12,
#           "192.168.123.22": 9,
#           "192.168.123.33": 54,
#           "192.168.123.44": 32
# }

ip_sort, ips = [], {"192.168.123.11": 12, "192.168.123.22": 9, "192.168.123.33": 54, "192.168.123.44": 32}
for item in ips.items():
    ip_sort.append(item)
for i in range(len(ip_sort)):
    for j in range(len(ip_sort) - 1):
        if ip_sort[j][1] > ip_sort[j+1][1]:
            ip_sort[j], ip_sort[j+1] = ip_sort[j+1], ip_sort[j]
print(dict(ip_sort))
