import json

# my_dict = {
#     'name': '骆昊',
#     'age': 40,
#     'friends': ['王大锤', '白元芳'],
#     'cars': [
#         {'brand': 'BMW', 'max_speed': 240},
#         {'brand': 'Audi', 'max_speed': 280},
#         {'brand': 'Benz', 'max_speed': 280}
#     ]
# }
# print(json.dumps(my_dict))

# with open('data.json', 'w') as file:
#     json.dump(my_dict, file)

data = {
    "name": "张三",
    "age": 30,
    "hobbies": ["编程", "读书"],
    "is_student": False
}

# 转换为JSON字符串（默认紧凑格式）
json_str = json.dumps(data)
print(json_str)  # {"name": "\u5f20\u4e09", "age": 30, ...}

# 美化输出（indent缩进，ensure_ascii禁用Unicode转义）
json_str_pretty = json.dumps(data, indent=2, ensure_ascii=False)
print(json_str_pretty)