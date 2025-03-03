class InputError(ValueError):
    """自定义异常类型"""
    pass


# def fac(num):
#     """求阶乘"""
#     if num < 0:
#         raise InputError('只能计算非负整数的阶乘')
#     if num in (0, 1):
#         return 1
#     return num * fac(num - 1)

# fac(5)
# print(dir(ImportError))

# try:
#     with open('致橡树.txt', 'r', encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('无法打开指定的文件!')
# except LookupError:
#     print('指定了未知的编码!')
# except UnicodeDecodeError:
#     print('读取文件时解码错误!')


try:
    with open('guido.jpg', 'rb') as file1:
        data = file1.read()
    with open('吉多.jpg', 'wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')