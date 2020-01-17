import re


data = 'Last login: Thu Mar  2 10:04:52 2019 from 39.100.110.135'
print(data.split())
print(re.split("[:. a]", data))

data = 'What is the difference between python 2.7.13 and python 3.7.3 ?'
# 去除上方数据源内的python版本号
result = re.findall("[1-9].[0-9].[0-9]{1,2}", data)
print(result)

object_re = re.compile("[1-9].[0-9].[0-9]{1,2}")
result = object_re.split(data)
print(result)

result = object_re.findall(data)
print(result)
