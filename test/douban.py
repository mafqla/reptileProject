# 爬取豆瓣
import re

import requests
from bs4 import BeautifulSoup


def get_html(url):
    # 获取网页源代码
    headers = {
        'User-Agent': 'Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"'
    }
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    html = res.text
    return html


# 正在热映
def get_hot_info(html):
    soup = BeautifulSoup(html, 'lxml')
    # 正在热映
    hot = soup.find('ul', class_='ui-slide-content')
    hot_list = hot.find_all('li', class_='ui-slide-item')
    for i in hot_list:
        # 电影id
        id = i.attrs['data-ticket']
        # 使用正则匹配数字
        id = re.findall(r'\d+', id)
        # print(id[0])
        # 图片
        img = i.find('img')
        img_url = img.attrs['src']
        # print(img.attrs['alt'])
        # 电影名
        name = i.find('li', class_='title')
        # print(name.text.split())
        # 上映时间
        time = i.attrs['data-release']
        # print(time)
        # 评分
        score = i.find('li', class_='rating')
        # print(''.join(score.text.split()))

        # 获取地区
        area = i.attrs['data-region']
        # print(area)

        # 通过数据库查询是否存在，并返回id
        sql = 'select id from country where name= %s'

        areacountry = select_data(sql, area)
        area = str(list(areacountry))
        # print(area)
        # print('id:', id[0], 'url:', img_url, 'name', img.attrs['alt'], 'score', img.attrs['alt'])
        data = {
            'id': id[0],
            'img': img_url,
            'title': img.attrs['alt'],
            'score': ''.join(score.text.split()),
            'time': time,
            'area': area,
            'titleName': 0
        }
        print(data)
        save_to_mysql(data)


# 最近热门电影
def get_hot_movie():
    headers = {
        'Host': 'movie.douban.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.5'
    }
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%97%A5%E6%9C%AC&page_limit=50&page_start=0'

    response = requests.get(url, headers=headers)
    # print(response.json())
    data = response.json()
    for i in data['subjects']:
        # id
        id = i['id']
        # img
        img = i['cover']
        # 电影名
        title = i['title']
        # 评分
        rate = i['rate']

        data = {
            'id': id,
            'img': img,
            'title': title,
            'rate': rate,
            'titleName': 1

        }
        print(data)
        save_to_mysql(data)


# 数据查询函数
def select_data(sqldata, area):
    import pymysql
    conn = pymysql.connect(host='localhost', user='root', password='123456', database='movie', charset='utf8')
    cursor = conn.cursor()
    # 接受为字符串
    sql = sqldata
    cursor.execute(sql, area)
    data = cursor.fetchone()
    # print(data)
    return data




# 热门推荐

def hot_recommend(html):
    soup = BeautifulSoup(html, 'lxml')
    # 热门推荐
    hot_recommend_data = soup.find('div', id='hot-gallery')
    # print(hot_recommend)
    hot_recommend_list = hot_recommend_data.find_all('li', class_='ui-slide-item')
    for i in hot_recommend_list:
        # 图片
        img = i.find('img')
        img_url = img.attrs['src']
        # print(img_url)
        # 标题
        h3 = i.find('h3')
        # print(h3.text)
        # 内容
        p = i.find('p')
        # print(p.text.strip())
        # 存进数组里
        data = {
            'img_url': img_url,
            'title': h3.text,
            'content': p.text.strip()
        }
        print(data)
        save_to_mysql(data)


#  最受欢迎的影评
def get_popular_review(html):
    soup = BeautifulSoup(html, 'lxml')
    # 最受欢迎的影评
    popular_review = soup.find_all('div', class_='review-list chart')

    for i in popular_review:
        # id
        con = i.find_all('div', class_='main review-item')
        for j in con:
            # print(j.attrs['id'])
            # 电影图片
            img = j.find('img')
            # print(img.attrs['src'])
            # 标题
            title = j.find('h2')
            # print(title.text)
            # 内容
            content = j.find('div', class_='short-content')
            content_text = re.sub(r'\s*', '', content.text).split('(展开)')[0]
            # print(content_text)
            # 评分
            score = j.find('span', class_='main-title-rating')
            # scoreClass = score.attrs['class'][0]
            try:
                scoreClass = score.attrs['class'][0]
            except AttributeError:
                scoreClass = '0'
            # 正则获取数字
            scoreNum = re.findall(r'\d+', scoreClass)[0]
            # 转化数字
            # print(int(scoreNum) / 10)
            # 发布时间
            time = j.find('span', class_='main-meta')
            # print(time.text)
            # 作者名
            author = j.find('a', class_='name')
            # print(author.text)
            # 作者头像
            author_img = j.find('a', class_='avator')
            # print(author_img.find('img').attrs['src'])
            # 赞同数
            agree = j.find('a', class_='action-btn up')
            # print(agree.find('span').text.strip())
            # 反对数
            disagree = j.find('a', class_='action-btn down')
            # print(disagree.find('span').text.strip())
            if disagree.find('span').text.strip() == '':
                disagreeNum = 0
            else:
                disagreeNum = disagree.find('span').text.strip()
            # 评论数
            comment = j.find('a', class_='reply')
            # print(comment.text.strip())
            # 使用正则获取数字
            commentNum = re.findall(r'\d+', comment.text.strip())[0]
            # print(commentNum)
            data = {
                'id': j.attrs['id'],
                'img': img.attrs['src'],
                'title': title.text,
                'content': content_text,
                'score': int(scoreNum) / 10,
                'time': time.text,
                'author': author.text,
                'author_img': author_img.find('img').attrs['src'],
                'agree': agree.find('span').text.strip(),
                'disagree': disagreeNum,
                'comment': commentNum

            }
            print(data)
            save_to_mysql(data)


# 数据库存储
def save_to_mysql(data):
    import pymysql
    conn = pymysql.connect(host='localhost', user='root', password='123456', database='movie', charset='utf8')
    cursor = conn.cursor()
    # sql = 'insert into movie(id,movie_img,name,times, rate, titlename,countid) values(%s,%s,%s,%s,%s,%s,%s)'
    # cursor.execute(sql, (
    # data['id'], data['img'], data['title'], data['time'], data['score'], data['titleName'], data['area']))
    sql = 'insert into movie(id,movie_img,name, rate, titlename) values(%s,%s,%s,%s,%s)'

    try:
        cursor.execute(sql, (data['id'], data['img'], data['title'], data['rate'], data['titleName']))
    except pymysql.err.IntegrityError:
        print('已存在')
        pass

    conn.commit()
    cursor.close()


def main():
    # url = 'https://movie.douban.com'
    url = 'https://movie.douban.com'
    html = get_html(url)
    # get_hot_info(html)
    # hot_recommend(html)
    # get_popular_review(html)
    get_hot_movie()


if __name__ == '__main__':
    main()
