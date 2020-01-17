import os
import fnmatch


for _, _, files in os.walk("files"):
    print(files)


# content = os.walk("files")
# print(list(content))

# 元组解包, 将元组中每个元素都等量的分给等量变量
# tupleA = (1, 2, 3)
# # a, b, c = tupleA
# # _, _, e = tupleA
# # print(a, b, c)
# # print(e)


# 使用os.walk寻找目录中符合条件的图片文件
result, images_format = [], ('*.jpg', '*.png', '*.jpeg', '*.tif', '*.tiff')
for root, dirs, files in os.walk("files"):
    for formats in images_format:
        for f in fnmatch.filter(files, formats):
            result.append(os.path.join(root, f))
print(result)

import sys

for i in range(10):
    if i % 3 == 0:
        sys.exit(200)


# python3 script.py
# if [ $? -ne 200 ];then
#    function
# fi
