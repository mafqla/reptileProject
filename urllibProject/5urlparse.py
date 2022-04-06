from urllib.parse import urlparse, urlunparse, urlunsplit, urlencode, quote, unquote
from urllib.parse import urlsplit

# 解析链接

result = urlparse('http://www.baidu.com/index.html;user?id=S#comment', scheme='https')
print(result)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')
result2 = urlsplit('http://www.baidu.com/index.html;user?id=S#comment', scheme='https')
print(result2)
print(result2.scheme, result2[0])

# urlunparse 长度必须为6
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
# urlunsplit 合并链接 长度必须为5
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6']
print(urlunsplit(data))

# urlencode 用于发送get请求参数
params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

# quote 将内容转换为url编码格式
keyword = '壁纸'
url2 = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url2)

# unquote URL编码格式解码

print(unquote(url2))