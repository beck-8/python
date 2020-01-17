import os



# 求1-100的累加和
sums = 0
for i in range(101):
    sums += i
print(sums)


def adds(n=10):
    if n == 0:
        return n
    return n + adds(n - 1)


# 1: n=10 + adds(n=10 - 1) -> 10 + adds(9)
# 2: 10 + n=9 + adds(n=9 - 1) ->
# ....
# 10: 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + adds(0)
print(adds(2))


dirC = fileC = 0
def getCount(path="/"):
    for files in os.listdir(path):
        fileAbs = os.path.join(path, files)
        if os.path.isdir(fileAbs):
            global dirC
            dirC += 1
            getCount(fileAbs)
        else:
            global fileC
            fileC += 1
    return dirC, fileC


dirCount, fileCount = getCount("/Users/liuchao/Documents")
print('dirCount: {}, fileCount: {}'.format(dirCount, fileCount))

