import requests
import pandas as pd
import time

# 接口 URL
url = "https://movie.douban.com/j/chart/top_list"

# 请求参数模板
param = {
    "type": "24",          # 电影类型，可修改
    "interval_id": "100:90",  # 评分区间
    "action": "",
    "start": 0,            # 起始位置
    "limit": 20,           # 每次抓取数量
}

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36"
}

# 存储抓取数据
all_movies = []

# 控制分页
while True:
    resp = requests.get(url, params=param, headers=headers)
    
    # 如果被反爬，返回内容可能不是 json
    try:
        data = resp.json()
    except:
        print("请求返回非 JSON，可能被反爬。")
        break

    # 如果没有数据，结束循环
    if not data:
        break

    # 遍历每条电影信息
    for item in data:
        movie = {
            "电影名": item.get("title", ""),
            "评分": item.get("score", ""),
            "评价人数": item.get("vote_count", ""),
            "海报": item.get("cover_url", ""),
            "详情页ID": item.get("id", "")
        }
        all_movies.append(movie)

    # 翻页
    param["start"] += param["limit"]
    
    # 控制抓取频率，防封
    time.sleep(1)

# 转为 DataFrame
df = pd.DataFrame(all_movies)

# 保存到 Excel
df.to_excel("douban_top_movies.xlsx", index=False)
print(f"抓取完成，共 {len(all_movies)} 条数据，已保存到 douban_top_movies.xlsx")
