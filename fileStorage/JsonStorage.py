# json文件存储

import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "2000-10-11"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "2991-12-12"
}, {
    "name": "问问",
    "gender": "女",
    "birthday": "2991-12-12"
}]
'''
# 读取
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))

# 写入
# ensure_ascii=False 用于输出中文
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))