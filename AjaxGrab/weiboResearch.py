import requests
from pymongo import MongoClient

# 保存到mongo数据库
from pyquery import PyQuery

client = MongoClient()
db = client['weibo']
collection = db['weiboSearch']
collectionHot = db['weiboTop']

# 微博热搜爬取
# 热搜api:https://weibo.com/ajax/side/hotSearch
base_url = 'https://weibo.com/ajax/side/hotSearch'
headers = {
    'Host': 'weibo.com',
    'referer': 'https://weibo.com/newlogin?tabtype=weibo&gid=102803&url=https%3A%2F%2Fweibo.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_page():
    url = base_url
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def get_top(json):
    if json:
        tops = json.get('data').get('hotgov')
        topTitle = {}
        topTitle['name'] = tops.get('name')
        topTitle['url'] = tops.get('url')
        topTitle['icon_desc'] = tops.get('icon_desc')
        yield topTitle


def parse_page(json):
    if json:
        items = json.get('data').get('realtime')
        for item in items:
            HotSearch = {}
            HotSearch['realpos'] = item.get('realpos')
            HotSearch['flag'] = item.get('flag')
            HotSearch['category'] = item.get('category')
            HotSearch['note'] = item.get('note')
            HotSearch['icon_desc'] = item.get('icon_desc')
            HotSearch['topic_flag'] = item.get('topic_flag')
            HotSearch['raw_hot'] = item.get('raw_hot')
            HotSearch['rank'] = item.get('rank')
            yield HotSearch


def save_to_weiboSearch(result):
    if collection.insert(result):
        print('Save to Mongo')


def save_to_weiboTop(topHot):
    if collectionHot.insert(topHot):
        print('Save to Mongo')


if __name__ == '__main__':
    json = get_page()
    topHots = get_top(json)
    results = parse_page(json)
    for result in results:
        print(result)
        save_to_weiboSearch(result)
    for topHot in topHots:
        print(topHot)
        save_to_weiboTop(topHot)
