import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 '
                  'Safari/537.36 Edg/96.0.1054.62'
}

r= requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('css-1g4zjtl.*?_blank.*?>(.*?)</a>', re.S)
title = re.findall(pattern, r.text)
# print(r.text)
print(title)