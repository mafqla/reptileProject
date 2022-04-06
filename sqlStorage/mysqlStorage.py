# mysql 数据库存取
import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# id = '20120001'
# user = 'Bob'
# age = 20
# cursor = db.cursor()
# # cursor.execute('SELECT VERSION()')
# # data = cursor.fetchone()
# # print('Database version:', data)
# # cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET  utf8")
# # db.close()
#
# # sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL , age INT NOT NULL, PRIMARY  KEY (id))'
# sql = 'INSERT INTO students(id, name, age) value (%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()
# db.close()

# 通过字典传值插入数据
# data = {
#     'id': '20120002',
#     'name': 'Bob',
#     'age': 20
# }
# cursor = db.cursor()
# table = 'students'
# keys = ', '.join(data.keys())
# values = ','.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# try:
#     if cursor.execute(sql, tuple(data.values())):
#         print("Successful")
#         db.commit()
# except:
#     print("Failed")
#     db.rollback()
# db.close()


# # 更新数据并插入数据
# data = {
#     'id': '20120002',
#     'name': 'Bob',
#     'age': 21
# }
# cursor = db.cursor()
# table = 'students'
# keys = ', '.join(data.keys())
# values = ','.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY  UPDATE '.format(table=table, keys=keys, values=values)
# update = ',' .join(["{key} = %s" .format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values())*2):
#         print("Successful")
#         db.commit()
# except:
#     print("Failed")
#     db.rollback()
# db.close()


# 删除数据
# table = 'students'
# condition = 'age > 20'
# cursor = db.cursor()
# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()


# 查询数据

sql = 'SELECT * FROM students WHERE age >=20'
cursor = db.cursor()
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Result Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')

