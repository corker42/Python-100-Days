# import random
# import time


# def download(filename):
#     """下载文件"""
#     print(f'开始下载{filename}.')
#     time.sleep(random.random() * 6)
#     print(f'{filename}下载完成.')

    
# def upload(filename):
#     """上传文件"""
#     print(f'开始上传{filename}.')
#     time.sleep(random.random() * 8)
#     print(f'{filename}上传完成.')

    
# download(r"MySql从删除到跑路")
# upload(r"Python从入门到住院.pdf")

# import time


# def record_time(func):

#     def wrapper(*args, **kwargs):
#         # 在执行被装饰的函数之前记录开始时间
#         start = time.time()
#         # 执行被装饰的函数并获取返回值
#         result = func(*args, **kwargs)
#         # 在执行被装饰的函数之后记录结束时间
#         end = time.time()
#         # 计算和显示被装饰函数的执行时间
#         print(f'{func.__name__}执行时间: {end - start:.2f}秒')
#         # 返回被装饰函数的返回值
#         return result
    
#     return wrapper

# download = record_time(download)
# upload = record_time(upload)
# download('MySQL从删库到跑路.avi')
# upload('Python从入门到住院.pdf')


# import random
# import time

# from functools import wraps


# def record_time(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'{func.__name__}执行时间: {end - start:.2f}秒')
#         return result

#     return wrapper


# @record_time
# def download(filename):
#     print(f'开始下载{filename}.')
#     time.sleep(random.random() * 6)
#     print(f'{filename}下载完成.')


# @record_time
# def upload(filename):
#     print(f'开始上传{filename}.')
#     time.sleep(random.random() * 8)
#     print(f'{filename}上传完成.')


# # 调用装饰后的函数会记录执行时间
# download('MySQL从删库到跑路.avi')
# upload('Python从入门到住院.pdf')
# # 取消装饰器的作用不记录执行时间
# download.__wrapped__('MySQL必知必会.pdf')
# upload.__wrapped__('Python从新手到大师.pdf')

# print("你好")

from functools import lru_cache


@lru_cache()
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 51):
    print(i, fib1(i))

