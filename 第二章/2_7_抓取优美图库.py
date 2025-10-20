# 1:拿到主页面的源代码，然后提取子页面的连接地址，href
# 2:通过href拿到子页面的内容，从子页面中找到图片的下载地址:img - > src
# 3:下载图片

import requests
from bs4 import BeautifulSoup
import time


url = "https://www.umei.cc/bizhitupian/weimeibizhi"
resp = requests.get(url)
# 处理乱码
resp.encoding = "utf-8"
main_page = BeautifulSoup(resp.text, "html.parser")
# 拿到所有a标签
alist = main_page.find("div", attrs={"class":"listlbc_cont_l"}).find_all("a")
for a in alist:
    # 得到子页面的链接
    child_url = url + (a.get("href") if a.get("href") else "")
    child_page_resp = requests.get(child_url)
    # 处理格式
    child_page_resp.encoding = "utf-8" 
    # 子页面的内容
    child_page_text = child_page_resp.text
    # 用BS4解析子页面
    child_page = BeautifulSoup(child_page_text, "html.parser")
    img = child_page.find("p", attrs={"align":"center"})
    img = p.find("img")
    # 得到图片的下载link
    src = img.get("src")
    img_resp = requests.get(src)
    # img_resp.content
    img_name = src.split("/")[-1]
    with open("img"+img_name, mode="wb") as f1:
        f1.write(img_resp.content)
    print("over!!!", img_name)
    time.sleep(1)
    
print("all over!!!")
