# 导入一个网络请求包
import requests
import time
# 导入一个正则表达式模块
import re
# 路径操作 进程管理
import os
import requests
from requests.adapters import HTTPAdapter

# 直接调用urllib3的disable_warnings()
import urllib3
urllib3.disable_warnings()
# 调用logging的captureWarnings()方法，传入True，关闭提示
import logging
logging.captureWarnings(True)

proxies = {
        'http': '127.0.0.1:1212',
        'https': '127.0.0.1:1212'
    }


count = 0

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}

url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1696314911322_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&sid=&word=%E8%80%81%E4%BA%BA%E9%9A%BE%E5%8F%97'

# TODO 增加连接重试次数(一共4次链接)
sess = requests.Session()
sess.mount('http://', HTTPAdapter(max_retries=3))
sess.mount('https://', HTTPAdapter(max_retries=3))
sess.keep_alive = False # 关闭多余连接


# 发送请求，指定了请求标头
html = requests.get(url=url, headers=header, stream=True, verify=False, proxies=proxies, timeout=20)
html.encoding = 'utf8'
# 转换成文本格式
html = html.text


# 将图片网址存储到一个list里面
img_url_list = re.findall('"objURL":"(.*?)"', html)
img_path = "./老人图片/"
# 指定一个保存地址
if not os.path.exists(img_path):
    os.mkdir(img_path)
for i in img_url_list:
    count += 1
    # 像图片的url发送请求
    img = requests.get(i)
    file_name = f'{img_path}picture{str(count)}.jpg'
    # 导入图片和音乐都会用wb的二进制导入方式
    f = open(file_name, 'wb')
    f.write(img.content)
    time.sleep(10)
