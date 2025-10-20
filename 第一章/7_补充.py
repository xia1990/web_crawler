import requests

url = "https://movie.douban.com/j/chart/top_list"
# 重新设置参数 
param = {
    "type":"24",
    "interval_id":"100:90",
    "action":"",
    "start":0,
    "limit":20,
}
heder = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36"
}
rsep = requests.get(url, params = param, headers = heder)
# print(rsep.request.url)
# 没有数据的话，又没有错误 ，证明你被反爬了
print(rsep.json())
# 关闭resp
rsep.close()
# print(rsep.request.headers)