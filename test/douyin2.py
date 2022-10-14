import os

import requests
import re
from selenium import webdriver
import time
from contextlib import closing


def get_home_ulrs(url):
    # 不显示浏览器
    options = webdriver.ChromeOptions()
    # 浏览器不显示
    options.add_argument('headless')
    browser = webdriver.Chrome(options=options)

    browser.get(url)
    time.sleep(2)
    # 关闭弹出框
    clone = '''
        document.querySelector('.mPWahmAI.screen-mask.login-mask-enter-done').remove()
    '''
    browser.execute_script(clone)
    time.sleep(2)
    temp_height = 0
    while True:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # time.sleep(2)

        # sleep一下让滚动条反应一下
        time.sleep(2)
        # 获取当前滚动条距离顶部的距离
        check_height = browser.execute_script(
            "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
        # 如果两者相等说明到底了
        if check_height == temp_height:
            break
        temp_height = check_height
    time.sleep(6)
    num = browser.find_elements_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[2]/div/ul/li/a')

    # 如果num是空的，重新获取一次
    if not num:
        num = browser.find_elements_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div/div[4]/div[1]/div[3]/ul/li/a')

    print(len(num))
    urls = []
    for i in num:
        # print(i.get_attribute('href'))
        link = i.get_attribute('href')
        urls.append(link)

    # print(set(urls))
    mainList = set(urls)
    browser.close()
    return mainList


def get_video(url):
    browser = webdriver.Chrome()
    browser.get(url)

    time.sleep(2)
    # 关闭弹出框
    clone = '''
        document.querySelector('.mPWahmAI.screen-mask.login-mask-enter-done').remove()
    '''
    browser.execute_script(clone)
    time.sleep(3)

    try:
        html = browser.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div/xg-video-container/video/source[1]')
    except Exception as e:
        if 'javascript error: Cannot read properties of null ' in str(e):
            print('出现滑块')
            time.sleep(30)
            # 重新获取一次
            html = browser.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div/xg-video-container/video/source[1]')
        else:
            print(e)
            return

    video_url = html.get_attribute('src')

    title = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div/h1/div/span[2]/span').text
    if not title:
        # 如果title为空，返回空

        title = 'none'
    # 点赞数
    like = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[1]').text
    # 评论数
    comment = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]').text
    # 收藏数
    collect = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[3]').text
    # 视频发布时间
    video_time = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/div[2]/span').text
    # 视频作者
    author = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/a/div/span/span/span/span/span/span').text

    info = f'{video_time}-标题-{title}-点赞-{like}评论-{comment}收藏-{collect}作者-{author}'
    # info转换为可以作为文件名的格式
    info = re.sub(r'[\\/:*?"<>|]', '-', info)
    print(info)
    browser.close()
    return video_url, info


def download(url, name):
    with closing(requests.get(url=url, verify=False, stream=True)) as res:
        with open(f'../dy_video/{name}.mp4', 'wb') as fd:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    fd.write(chunk)


def check_file(name):
    # 读取文件夹，查看视频是否已经下载过
    for root, dirs, files in os.walk('../dy_video'):
        for file in files:
            if file == f'{name}.mp4':
                return True
    return False


if __name__ == '__main__':
    # url = input('请输入个人主页地址')
    url = 'https://www.douyin.com/user/MS4wLjABAAAAqy1OO-UP9J2LJ1xSg_lsryKCicbLFLGzBgTRRT4W14Y?showTab=like'
    print('正在获取视频地址')
    urls = get_home_ulrs(url)
    # print(urls)
    print('成功获取{}个,开始下载'.format(len(urls)))
    index = 1
    for url in urls:
        get_video_url = get_video(url)
        try:
            v_url = get_video_url[0]
            v_title = get_video_url[1]
            if check_file(v_title):
                print(f'{v_title}已经下载过了')
                continue
            print('正在下载{}/{}'.format(len(urls), v_title))
            download(v_url, v_title)
            print('下载完成')
            index += 1
            print('正在下载第{}个视频'.format(index))
        except Exception as e:
            print(e)
            # 如果出现错误，跳过这个视频
            if 'no such element: Unable to locate element' in str(e):
                continue
