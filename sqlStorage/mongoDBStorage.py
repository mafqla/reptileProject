import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
# db = client.test
# collection = db.students
# student = {
#     'id': '201902101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)
#
# # 插入多条数据
# student1 = {
#     'id': '201902102',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# student2 = {
#     'id': '201902103',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# result2 = collection.insert_many([student1, student2])
# print(result2)
# print(result2.inserted_ids)


# 数据查询
'''
$lt  小于  {'age':{'$lt':20}}
$gt  大于  {'age':{'$gt':20}}
$lte 小于等于  {'age':{'$lte':20}}
$gte 大于等于  {'age':{'$gte':20}}
$ne  不等于  {'age':{'$ne':20}}
$in  在范围内  {'age':{'$in': [20,23]}}
$nin 不在范围  {'age':{'$nin': [20,23]}}
'''
# results = collection.find({'age': 20})
# print(results)
# for result in results:
#     print(result)
#
# result2 = collection.find({'age': {'$gt': 20}})
# print(result2)
# 利用正则表达式查询
'''
$regex  匹配正则表达式 {'name' : {’ $reg ex ’ : ''M. *'}}  name 以 M 开头
$exists 属性是否存在   {'name ’·{’$exists' : True}}       name 属性存在
$type 类型判断        {'age':{ '$type': 'int'}}          age 的类型为 int
$mad  数字模操作      {'age' : ｛'$mad': [5,0]}}          年龄模5余0
$text 文本查询        {'$text': {'$search': 'Mike'}}    text 类型的属性中包含 Mike
                                                       字符串
$where 高级条件查询 {'$where': obj.fans＿count == obj. follows_ count'} 自身粉丝数等于关注数
'''
db = client['weibo']
collection = db['weibo']
results = collection.find({'id': 4722401759723744})
print(results)
for result in results:
    print(result)
# result3 = collection.find({'name': {'$regex': '^M.*'}})
# print(result3)
#
# # 统计数量
# count = collection.find({'age': 20}).count()
# print(count)
#
# # 偏移 skip()方法
#
# result4 = collection.find().sort('name', pymongo.ASCENDING).skip(2)
# print([result['name'] for result in result4])

# 更新数据 update_one()
# condition = {'name': 'Kevin'}
# student = collection.find_one(condition)
# student['age'] = 26
# result = collection.update_one(condition, {'$set': student})
# print(result)
# print(result.matched_count, result.modified_count)


# 条件查询  match_count 匹配的数据条数  modified_count 影响的数据条数
# condition = {'age': {'$gt': 20}}
# result = collection.update_one(condition, {'$inc': {'age': 1}})
# print(result)
# print(result.matched_count, result.modified_count)

# condition = {'age': {'$gte': 20}}
# result = collection.update_many(condition, {'$inc': {'age': 1}})
# print(result)
# print(result.matched_count, result.modified_count)

# 删除 delete_one() delete_many

# result = collection.delete_one({'name': 'Kevin'})
# print(result)
# print(result.deleted_count)
# result = collection.delete_many({'age': {'$gt': 25}})
# print(result.deleted_count)
