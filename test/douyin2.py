import requests
import re
from selenium import webdriver
import time
from contextlib import closing


def get_home_ulrs(url):
    browser = webdriver.Chrome()
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
        time.sleep(3)
        # 获取当前滚动条距离顶部的距离
        check_height = browser.execute_script(
            "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
        # 如果两者相等说明到底了
        if check_height == temp_height:
            break
        temp_height = check_height

    time.sleep(3)
    num = browser.find_elements_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[2]/div/ul/li/a')

    # 如果num是空的，重新获取一次
    if not num:
        num = browser.find_elements_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[2]/div/ul/li/a')


    print(len(num))
    urls = []
    for i in num:
        print(i.get_attribute('href'))
        link = i.get_attribute('href')
        urls.append(link)

    print(set(urls))
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
    time.sleep(2)

    html = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div/xg-video-container/video/source[1]')
    video_url = html.get_attribute('src')

    title = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div/h1/div/span[2]/span/span/span/span/span').text
    video_info = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div[2]').text
    # 视频作者
    author = browser.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/a/div/span/span/span/span/span/span').text

    print(title, video_info, author)
    browser.close()
    return video_url


def download(url, name):
    with closing(requests.get(url=url, verify=False, stream=True)) as res:
        with open(f'../dy_video/{name}.mp4', 'wb') as fd:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    fd.write(chunk)


if __name__ == '__main__':
    # url = input('请输入个人主页地址')
    url = 'https://www.douyin.com/user/MS4wLjABAAAAqy1OO-UP9J2LJ1xSg_lsryKCicbLFLGzBgTRRT4W14Y?showTab=like'
    print('正在获取视频地址')
    urls = get_home_ulrs(url)
    print(urls)
    print('成功获取{}个,开始下载'.format(len(urls)))
    index = 1
    for url in urls:
        video_url = get_video(url)
        print('正在下载{}/{}'.format(len(urls), index))
        download(video_url, index)
        print('下载完成')
        index += 1
