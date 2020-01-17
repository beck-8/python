# python中装饰器, 就是用来对函数进行装饰的
# 装饰器依赖于函数闭包

import time


# UTC: 就是从1979年1月1号00:00:00开始到现在秒数
start_time = time.time()

for i in range(1000):
    print(i)

end_time = time.time()

print("相差时间为: {}".format(end_time - start_time))

# 将计算时间差的程序, 做到高度复用;
# def times(function):
#     start_time = time.time()
#     function()
#     end_time = time.time()
#     print("相差时间为: {}".format(end_time - start_time))
import functools

def times(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        return end_time - start_time
    return wrapper

@times   # 语法糖
def cycle(number):
    for i in range(number):
        print(i)


# 普通调用装饰器
# f01 = times(cycle)
# timess = f01(10000)   -> cycle(10000)
# print(timess)

# timess = cycle(100000)
# print(timess)


# 被装饰的函数, 还是不是自己?
print(cycle.__name__)


# 验证函数的登录 user load
users = {'tom': '123456', 'jerry': 'jerry123', 'hale': 'hale123'}
def user_load_check(function):
    def wrapper(user, password, *args):
        if user in users.keys() and password == users[user]:
            print("装饰器检查用户名和密码正确")
            function(user, password, *args)
        else:
            print("请检查您的用户名和密码!")
    return wrapper

# welcome page:
@user_load_check
def welcome(user, password):
    print("index.php: hello {}".format(user))

# 收藏商品
@user_load_check
def save(user, password, product):
    print("product's page: 您收藏了: {}".format(product))

# 模拟用户登录
welcome("tom", "12345")

save("tom", "123456", "娃娃")


