# step1:拿到页面源代码  requests
# step2:使用正则提取需要的有效信息  re
import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)
page_content = resp.text
pattern = (
    r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
    r'.*?<p>.*?<br>(?P<year>.*?)&nbsp.*?'
    r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
    r'.*?<span>(?P<num>.*?)人评价</span>'
)
obj = re.compile(pattern, re.S)
result = obj.finditer(page_content)
f = open("data.csv", mode="w")
csvwriter = csv.writer(f)
for it in result:
    # print(it.group("name"))
    # print(it.group("score"))
    # print(it.group("year").strip())
    # print(it.group("num"))
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
print("over!")
    