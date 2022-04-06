import urllib.request
import urllib.error
import socket
from urllib import request, parse

'''

response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
'''

'''
try:
    response = urllib.request.urlopen('https://www.python.org', timeout=10.0)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
'''

'''
data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data, timeout=2.0)
print(response.read().decode('utf-8'))
'''

'''
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=urllibProject.0)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
'''

'''
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
'''

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9473',
    'https': 'https://127.0.0.1:9473'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)


