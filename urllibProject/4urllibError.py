import socket
import urllib.request
import urllib.error

# 错误抛出
try:
    response = urllib.request.urlopen('https://skyseek.top')
except urllib.error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except urllib.error.URLError as e:
    print(e.reason)
else:
    print("request successfully")