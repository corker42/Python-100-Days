# import openpyxl
# import datetime

# import os

# # 方法1：假设文件与脚本同级
# file_relative = '阿里巴巴2020年股票数据.xlsx'
# print("方法1路径:", os.path.abspath(file_relative))

# # 方法2：动态获取脚本所在目录
# script_dir = os.path.dirname(os.path.abspath(__file__))
# file_absolute = os.path.join(script_dir, '阿里巴巴2020年股票数据.xlsx')
# print("方法2路径:", file_absolute)

# # 检查文件是否存在
# if os.path.exists(file_absolute):
#     print("文件存在！")
# else:
#     print("文件不存在！请检查路径或文件位置")

# # 打印当前工作目录
# print("当前工作目录:", os.getcwd())
# # 打印文件绝对路径
# print("文件绝对路径:", os.path.abspath('阿里巴巴2020年股票数据.xlsx'))



# file_path = '阿里巴巴2020年股票数据.xlsx'
# if os.path.exists(file_path):
#     print("文件存在")
# else:
#     print("文件不存在")

# # 打开Excel文件
# wb = openpyxl.load_workbook('阿里巴巴2020年股票数据.xlsx')
# # 获取所有表单名称
# sheetnames = wb.sheetnames
# print(sheetnames)

# # 获取第一个工作表
# sheet = wb[sheetnames[0]]
# # 获取行数和列数
# print(sheet.max_row, sheet.max_column)

# for row in sheet.iter_rows(values_only=True):
#     for idx, value in enumerate(row):
#         # 处理日期列（假设日期在第1列，索引从0开始）
#         if idx == 0 and isinstance(value, datetime.datetime):
#             value = value.strftime('%Y年%m月%d日')
#         # 处理数值列（保留两位小数）
#         elif isinstance(value, (int, float)):
#             value = f'{value:.2f}'
#         print(value, end='\t')
#     print()

# # 获取最后一个单元格的数据类型
# last_cell = sheet.cell(sheet.max_row, sheet.max_column)
# print(last_cell.data_type)  # 输出类型代码（n=数字，s=字符串，d=日期等）

# # 获取第一行的值
# print([cell.value for cell in sheet[1]])

# # 获取指定行范围的数据（例如第4行，列0到4）
# print([cell.value for cell in sheet[4]][0:5])


import random

import xlwt

student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
scores = [[random.randrange(50, 101) for _ in range(3)] for _ in range(5)]
# 创建工作簿对象（Workbook）
print(len(scores))
print(len(scores[0]))
wb = xlwt.Workbook()
# 创建工作表对象（Worksheet）
sheet = wb.add_sheet('一年级二班')
# 添加表头数据
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    sheet.write(0, index, title)
# 将学生姓名和考试成绩写入单元格
for row in range(len(scores)):
    sheet.write(row + 1, 0, student_names[row])
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1, scores[row][col])
# 保存Excel工作簿
wb.save('考试成绩表.xlsx')