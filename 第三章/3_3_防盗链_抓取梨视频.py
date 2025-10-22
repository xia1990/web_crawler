# 1：得到countId
# 2：
# 实际连接：https://video.pearvideo.com/mp4/short/20251020/cont-1803044-16064059-hd.mp4
import requests


base_url = "https://www.pearvideo.com/video_1803044"
countID = base_url.split("_")[1]

url = f"https://www.pearvideo.com/videoStatus.jsp?contId={countID}&mrd=0.3399017052541303"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    # 防盗链 -> 溯源 -> 本次请求的上一级
    "referer": base_url
}
resp = requests.get(url, headers = headers)
data = resp.json()
print(type(data))
# 实际视频地址
# https://image.pearvideo.com/cont/20251020/cont-1803044-12790914.mp4
srcUrl = data.get("videoInfo").get("videos").get("srcUrl")
systemTime = data.get("systemTime")
# 根据实际视频地址，进行替换
video_url = srcUrl.replace(systemTime, "cont-"+countID)
# 下载视频
with open("a.mp4", mode = "wb") as f:
    f.write(requests.get(video_url).content)