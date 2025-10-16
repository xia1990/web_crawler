import requests

url = "https://so.news.cn/getNews?lang=ru&curPage=73&searchFields=0&sortField=0&keyword=%D0%A1%D0%B8%D0%BD%D1%8C%D1%86%D0%B7%D1%8F%D0%BD"

heder = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36"
}
rsep = requests.get(url, headers = heder)
# print(rsep.request.url)
# 没有数据的话，又没有错误 ，证明你被反爬了
print(rsep)
print(rsep.json())
