# 安装requests
# pip install requests
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

import requests
query = input("输入一个你喜欢的明星")

url = f'https://www.sogou.com/web?query={query}'

dic = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}

resp = requests.get(url, headers=dic) #处理一个小小的反爬

print(resp)
print(resp.text) #拿到页面源代码