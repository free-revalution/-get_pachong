#拿到页面源代码。  requests
#通过re来提取想要的有效信息  re
import requests
import re
import csv

url = "https://movie.douban.com/top250?start=0&filter="
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}
resp = requests.get(url, headers=headers)
page_content = resp.text

#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" '
                 r'property="v:average">(?P<score>.*?)</span>.*?<span>(?P<comment>.*?)</span>', re.S)
#开始匹配
result = obj.finditer(page_content)
f = open("data.csv", mode="w")
csvwriter = csv.writer(f)
for it in result:
    '''
    print(it.group("name"))
    print(it.group("score"))
    print(it.group("comment"))
    print(it.group("year").strip())
    '''
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
print("over!")


