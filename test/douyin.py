# 抖音水印去除

import requests
import re
import os
from selenium import webdriver

header = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39 '
}


def get_video_id(video_url):
    """
    根据视频链接，获得视频的id
    """
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                        'like Gecko) Chrome/96.0.4664.110 Safari/537.36')
    driver = webdriver.Chrome(options=option)
    driver.get(video_url)
    # 获得源码
    html = driver.page_source

    id_pattern = '<div class="IsE_azet">.*?from_gid=(.*?)&'
    video_id = re.findall(id_pattern, html)

    return video_id[0]


def get_video_info(video_id):
    """
    利用video_id 获得视频的一些信息，作者，无水印链接等
    """
    video_info_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={video_id}'

    # 获得视频的信息
    resp = requests.get(video_info_url, headers=header)
    video_info_json = resp.json()
    resp.close()

    # 获取作者名字
    author_name = video_info_json['item_list'][0]['author']['nickname']
    # 获取视频标题
    video_title_tmp = video_info_json['item_list'][0]['share_info']['share_title']
    if video_title_tmp.startswith('#'):
        video_title = video_title_tmp.split('#')[1].split('@')[0]
    else:
        video_title = video_title_tmp.split('#')[0].split('@')[0]
    # 用于保存文件的名字
    title = author_name + '-' + video_title + '-' + video_id
    # 获取视频的无水印地址,wm=watermark
    video_true_url = video_info_json['item_list'][0]['video']['play_addr']['url_list'][0].replace('/playwm/', '/play/')

    return title, video_true_url


def download(title, video_true_url):
    """
    下载视频
    """
    # 创建存放位置
    path = '../dy_video'
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)

    # 获取视频
    resp = requests.get(video_true_url, headers=header)
    content = resp.content
    resp.close()
    # 下载视频
    with open(f'../dy_video/{title}.mp4', 'wb') as f:
        f.write(content)

    print("视频下载完成！")
    print(f"视频名字为：{title}.mp4")


def main():
    """
    主程序
    """
    url_or_id = str(input("输入分享链接或者视频id："))
    if len(url_or_id) == 19:
        # 长度小于30，是一个视频id,id长度为19
        print('输入的是视频id。')
        title, video_true_url = get_video_info(url_or_id)
        download(title, video_true_url)
    else:
        # 是一个分享链接
        print('输入的是视频分享链接。')
        video_url = url_or_id.split(" ")[-2]
        video_id = get_video_id(video_url)
        title, video_true_url = get_video_info(video_id)
        download(title, video_true_url)


if __name__ == '__main__':
    main()