﻿# import sys
# print(sys.executable)

"""
要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re

# username = input('请输入用户名: ')
# qq = input('请输入QQ号: ')
# # match函数的第一个参数是正则表达式字符串或正则表达式对象
# # match函数的第二个参数是要跟正则表达式做匹配的字符串对象
# m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
# if not m1:
#     print('请输入有效的用户名.')
# # fullmatch函数要求字符串和正则表达式完全匹配
# # 所以正则表达式没有写起始符和结束符
# m2 = re.fullmatch(r'[1-9]\d{4,11}', qq)
# if not m2:
#     print('请输入有效的QQ号.')
# if m1 and m2:
#     print('你输入的信息是有效的!')


sentence = 'Oh, shit! 你是傻逼吗? Fuck you.'
purified = re.sub('fuck|shit|[傻煞沙][比笔逼叉缺吊碉雕]',
                  '*', sentence, flags=re.IGNORECASE)
print(purified)  # Oh, *! 你是*吗? * you.

poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentences_list = re.split(r'[，。]', poem)
print(sentences_list)
sentences_list = [sentence for sentence in sentences_list if sentence]
for sentence in sentences_list:
    print(sentence)