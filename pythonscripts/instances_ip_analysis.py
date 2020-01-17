# with open("files/access.log", "r", encoding="utf8") as log:
#     # read() // readline() // readlines()
#     # 不能这么用,但是用起来很好用的方法;
#     ips = {}
#     for lines in log.readlines():
#         if lines.split()[6] in ips.keys():
#             ips[lines.split()[6]] += 1
#         else:
#             ips[lines.split()[6]] = 1
#     print(ips)
#     ip_sort = []
#     for item in ips.items():
#         ip_sort.append(item)
#     for i in range(len(ip_sort)):
#         for j in range(len(ip_sort) - 1):
#             if ip_sort[j][1] < ip_sort[j + 1][1]:
#                 ip_sort[j], ip_sort[j + 1] = ip_sort[j + 1], ip_sort[j]
#     print(dict(ip_sort[:3]))

with open("files/access.log", "r", encoding="utf8") as log:
    ips = {}
    while True:
        lines = log.readline()
        if not bool(lines):
            break
        if lines.split()[0] in ips.keys():
            ips[lines.split()[0]] += 1
        else:
            ips[lines.split()[0]] = 1
    print(ips)
    ip_sort = []
    for item in ips.items():
        ip_sort.append(item)
    for i in range(len(ip_sort)):
        for j in range(len(ip_sort) - 1):
            if ip_sort[j][1] < ip_sort[j + 1][1]:
                ip_sort[j], ip_sort[j + 1] = ip_sort[j + 1], ip_sort[j]
    print(dict(ip_sort[:3]))


