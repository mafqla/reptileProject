import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.ExploreHomePage').items()
for item in items:
    question = item.find('.css-1as7ang a').text()
    print(question)
    author = item.find('.css-13jrecd').text()
    print(author)
    answer = pq(item.find('.css-13jrecd').html()).text()
    print(answer)
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()