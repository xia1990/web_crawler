import requests
from bs4 import BeautifulSoup
import sys

url = "http://www.xinfadi.com.cn/getPriceData.html"
headers = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36"
}
resp = requests.get(url)
print(resp.json())
sys.exit()
page = BeautifulSoup(resp.text, "html.parser")
# clsss 是python关键字
# tbody = page.find("table", class_="hq_table")
div = page.find("div", attrs={"class":"tablebox"})
print(div)