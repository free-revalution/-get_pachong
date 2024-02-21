#1.拿到主页面的源代码，然后提取到子页面的链接地址，href
#2.通过href拿到子页面的内容，充值页面中找到图片的下载地址 img -> src
#3.下载图片

import requests
from bs4 import BeautifulSoup
import time


url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8' #处理乱码
#把源代码交给bs
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="listlbc_cont_l").find_all("a") #把范围第一次缩小


for a in alist:
    href_1 = a.get('href') #直接通过get就可以拿到属性的值
    w = "https://www.umei.cc/"
    href = w + href_1.strip("/")

    #拿到子页面的源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text

    #从子页面中拿到图片的下载路径

    child_page = BeautifulSoup(child_page_text, "html.parser")
    p = child_page.find("div", class_="big-pic")
    img = p.find("img")
    src = img.get("src")
    #下载图片
    img_resp = requests.get(src)
    #img_resp.content 这里拿到的是字节
    img_name = src.split("/")[-1]    #拿到url中最后一个/以后的内容
    with open("C:\Users\DELL\PycharmProjects\opencv\图片"+img_name, mode="wb") as f:
        f.write(img_resp.content)   #图片内容写入文件

    print("over!", img_name)
    time.sleep(1)

print("all over!")






