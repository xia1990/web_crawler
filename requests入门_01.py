# pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple requests

import requests

query = input("输入一个你喜欢的明星：")
url = f'https://www.sogou.com/web?query={query}'
dic = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36"
}

resp = requests.get(url, headers = dic)
# 返回的是响应码，成功为：200
print(resp)
# 得到页面源代码
print(resp.text)