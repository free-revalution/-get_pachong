#拿到页面源代码
#提取和解析数据

import requests
from lxml import etree


url = "https://huaian.zbj.com/search/service/?kw=saas&r=2"
resp = requests.get(url)
#print(resp.text)
#解析
html = etree.HTML(resp.text)
#拿到每一个服务商的div
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div')
for div in divs:  #每一个服务商的信息
    price = div.xpath("./div/div/div[1]/span/text()")[0].strip("￥")
    title = "saas".join(div.xpath("./"))
    com_name = div.xpath()[0]
    location = div.xpath()[0]
    print(price)