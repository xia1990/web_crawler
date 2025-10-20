# 屠戮：nfnw
# 1：从主页面定位到2020必看篇
# 2：从2020必看篇中提取到子页面的url
# 3：请求子页面的连接地址，拿到我们想要的电影片名和下载地址.............
import requests
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
domain = "https://www.dytt8899.com"
# verify=False 去掉安全验证
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
resp = requests.get(domain, verify=False)
# 指定字符集
resp.encoding = "gb2312"
content =resp.text
with open("move.html", mode="w") as f:
    f.write(content)
# 拿到ul中的li
obj1 = re.compile(r"2025必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(
    r'◎片　　名(?P<movie>.*?)<br />.*?<td '
    r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)>', re.S)


result = obj1.finditer(content)

child_href_list = []
for it in result:
    # 主页面的 ul
    ul = it.group("ul")
    # print(ul)
    for it2 in obj2.finditer(ul):
        # 子页面的 url
        child_url = domain + it2.group("href")
        child_href_list.append(child_url)

for url in child_href_list:
    resp2 = requests.get(url)
    resp2.encoding = "gb2312"
    child_content = resp2.text
    with open("child.html", mode="w") as f1:
        f1.write(child_content)

    result2 = obj3.finditer(child_content)
    for it3 in result2:
        print(it3.group("movie"),":",it3.group("download"))
    

