from urllib.parse import urlencode
import requests
from pymongo import MongoClient
from pyquery import PyQuery

base_url = 'https://weibo.com/ajax/feed/hottimeline?'

headers = {
    'Host': 'weibo.com',
    'referer': 'https://weibo.com/newlogin?tabtype=weibo&gid=102803&url=https%3A%2F%2Fweibo.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    'X-Requested-With': 'XMLHttpRequest'
}
# 保存到mongo数据库
client = MongoClient()
db = client['weibo']
collection = db['weibo']


def get_page():
    params = {
        'refresh': 2,
        'group_id': 102803,
        'containerid': 102803,
        'extparam': 'discover|new_feed',
        'max_id': 4,
        'count': 10
    }
    url = base_url + urlencode(params)
    # print(url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        items = json.get('statuses')
        for item in items:
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['datatime'] = item.get('created_at')
            weibo['source'] = item.get('source')
            weibo['text'] = PyQuery(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo


def save_to_mongo(result):
    if collection.insert(result):
        print('Save to Mongo')


if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page()
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)
