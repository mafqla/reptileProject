# post 请求
import requests

data = {'name': 'germey', 'age': '22'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
r2 = requests.get("http://www.jianshu.com")
print("状态码:", r2.status_code, type(r2.status_code))
print("请求头:", type(r2.headers), r2.headers)
print("cookies:", type(r2.cookies), r2.cookies)
print("URL:", type(r2.url), r.url)
print("请求历史:", type(r.history), r.history)

# 文件上传

files = {'file': open('favicon.ico', 'rb')}
r3 = requests.post("http://httpbin.org/post", files=files)
print(r3.text)

r4 = requests.get('https://www.12306.cn')
print(r4.status_code)

# 登陆验证方法
# 认证成功返回200，认证失败返回401
r5 = requests.get('http://120.24.185.28:9000/', auth=('username', 'password'))
print(r5.status_code)
