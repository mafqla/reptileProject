"""
模式	描述
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
U	通用换行模式（Python 3 不支持）。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""
# csv 存取
import csv

# 写入
with open('data.csv', 'w') as csvfile:
    # delimiter 修改行分隔符
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1001', 'Mike', '20'])
    writer.writerow(['1002', 'Bob', '22'])
    writer.writerow(['1003', 'Jordan', '21'])

# 字典写入

with open('dataItem.csv', 'w', encoding='utf-8') as itemfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(itemfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '1001', 'name': 'Mike', 'age': '12'})
    writer.writerow({'id': '1002', 'name': 'Bob', 'age': '22'})
    writer.writerow({'id': '1003', 'name': 'Morty', 'age': '32'})


# 读取

with open('data.csv', 'r', encoding='utf-8') as csvread:
    reader = csv.reader(csvread)
    for row in reader:
        print(row)


# 利用pandas库读取csv
import pandas as pd
df = pd.read_csv('data.csv')
print(df)