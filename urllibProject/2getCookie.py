# 获取cookie
import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://baidu.com')
# for item in cookie:
#     print(item.name+"="+item.name)


# 保存cookie文件格式

# filename = 'cookies.txt'
# # cookie = http.cookiejar.MozillaCookieJar(filename)
# # 保存为LWP格式
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)


cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
