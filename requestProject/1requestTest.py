import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
# print(r.text.encode('utf-8'))
print(r.cookies)

print('----------------------------------')
r2 = requests.get('http://httpbin.org/get')
print(r2.text)
print(r2.json())
print(type(r2.json()))
print('----------------------------------')
data = {
    'name': 'germey',
    'age': "22"
}
r3 = requests.get("http://httpbin.org/get", params=data)
print(r3.text)
